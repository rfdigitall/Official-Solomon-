(function () {
  'use strict';

  const hamburger = document.getElementById('hamburger');
  const nav = document.getElementById('nav');

  if (hamburger && nav) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('open');
      nav.classList.toggle('open');
    });

    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('open');
        nav.classList.remove('open');
      });
    });
  }

  const navLinks = document.querySelectorAll('.nav a');
  const sections = document.querySelectorAll('section[id]');

  if (navLinks.length && sections.length) {
    const navObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        navLinks.forEach(link => {
          link.classList.toggle('active', link.getAttribute('href') === '#' + entry.target.id);
        });
      });
    }, { threshold: 0.4, rootMargin: '-20% 0px -55% 0px' });

    sections.forEach(section => navObserver.observe(section));
  }

  const animateEls = document.querySelectorAll('[data-animate]');

  if (animateEls.length) {
    const revealObserver = new IntersectionObserver(entries => {
      entries.forEach((entry, index) => {
        if (!entry.isIntersecting) return;
        setTimeout(() => {
          entry.target.classList.add('is-visible');
        }, index * 60);
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    animateEls.forEach(el => revealObserver.observe(el));
  }

  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxClose = document.getElementById('lightboxClose');

  if (lightbox && lightboxImg) {
    document.querySelectorAll('.gallery-item').forEach(item => {
      item.addEventListener('click', () => {
        const img = item.querySelector('img');
        if (!img) return;
        lightboxImg.src = img.src;
        lightboxImg.alt = img.alt;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
      });
    });

    function closeLightbox() {
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
      setTimeout(() => lightboxImg.removeAttribute('src'), 300);
    }

    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', e => {
      if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeLightbox();
    });
  }

  const hero = document.getElementById('home');
  const heroBg = document.getElementById('heroBg');

  if (hero && heroBg && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    let ticking = false;

    function updateParallax() {
      const rect = hero.getBoundingClientRect();
      const viewH = window.innerHeight;

      if (rect.bottom > 0 && rect.top < viewH) {
        const offset = -rect.top * 0.18;
        heroBg.style.setProperty('--hero-parallax', offset + 'px');
      }

      ticking = false;
    }

    window.addEventListener('scroll', () => {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(updateParallax);
      }
    }, { passive: true });

    updateParallax();
  }

  /* ── Geolocalizzatore ── */
  const geoMapEl = document.getElementById('geoMap');
  const geoLocateBtn = document.getElementById('geoLocateBtn');
  const geoStatus = document.getElementById('geoStatus');
  const geoDetails = document.getElementById('geoDetails');
  const geoAddress = document.getElementById('geoAddress');
  const geoCoords = document.getElementById('geoCoords');
  const geoAccuracy = document.getElementById('geoAccuracy');
  const geoShareActions = document.getElementById('geoShareActions');
  const geoWhatsAppBtn = document.getElementById('geoWhatsAppBtn');
  const geoMapsBtn = document.getElementById('geoMapsBtn');
  const geoCopyBtn = document.getElementById('geoCopyBtn');

  const BRESCIA_CENTER = [45.5416, 10.2118];
  const WHATSAPP_NUMBER = '393395998469';
  let geoMap = null;
  let userMarker = null;
  let accuracyCircle = null;
  let currentPosition = null;

  function formatCoords(lat, lng) {
    return lat.toFixed(5) + ', ' + lng.toFixed(5);
  }

  function mapsUrl(lat, lng) {
    return 'https://www.google.com/maps?q=' + lat + ',' + lng;
  }

  function whatsAppShareUrl(lat, lng, address) {
    const link = mapsUrl(lat, lng);
    const text = [
      'Ciao, sono in panne e ho bisogno di assistenza.',
      '',
      address ? 'Posizione: ' + address : '',
      'Coordinate: ' + formatCoords(lat, lng),
      'Mappa: ' + link
    ].filter(Boolean).join('\n');
    return 'https://wa.me/' + WHATSAPP_NUMBER + '?text=' + encodeURIComponent(text);
  }

  function setGeoStatus(message, type) {
    if (!geoStatus) return;
    geoStatus.classList.remove('is-success', 'is-error');
    if (type) geoStatus.classList.add('is-' + type);
    geoStatus.querySelector('p').textContent = message;
  }

  async function reverseGeocode(lat, lng) {
    try {
      const url = 'https://nominatim.openstreetmap.org/reverse?format=json&lat=' +
        lat + '&lon=' + lng + '&accept-language=it&zoom=18';
      const res = await fetch(url, {
        headers: { 'Accept': 'application/json' }
      });
      if (!res.ok) return '';
      const data = await res.json();
      return data.display_name || '';
    } catch {
      return '';
    }
  }

  function updateShareLinks(lat, lng, address) {
    if (geoWhatsAppBtn) geoWhatsAppBtn.href = whatsAppShareUrl(lat, lng, address);
    if (geoMapsBtn) geoMapsBtn.href = mapsUrl(lat, lng);
    if (geoShareActions) geoShareActions.hidden = false;
  }

  function showPosition(lat, lng, accuracy) {
    currentPosition = { lat, lng, accuracy };

    if (geoCoords) geoCoords.textContent = formatCoords(lat, lng);
    if (geoAccuracy) {
      geoAccuracy.textContent = accuracy
        ? '± ' + Math.round(accuracy) + ' metri'
        : 'Non disponibile';
    }
    if (geoDetails) geoDetails.hidden = false;

    if (geoMap) {
      if (userMarker) geoMap.removeLayer(userMarker);
      if (accuracyCircle) geoMap.removeLayer(accuracyCircle);

      userMarker = L.marker([lat, lng], {
        icon: L.divIcon({
          className: 'geo-marker-user-wrap',
          html: '<span class="geo-marker-user"></span>',
          iconSize: [18, 18],
          iconAnchor: [9, 9]
        })
      }).addTo(geoMap);

      if (accuracy) {
        accuracyCircle = L.circle([lat, lng], {
          radius: accuracy,
          color: '#ffb400',
          fillColor: '#ffb400',
          fillOpacity: 0.12,
          weight: 1
        }).addTo(geoMap);
      }

      geoMap.setView([lat, lng], accuracy && accuracy < 80 ? 16 : 14, { animate: true });
      setTimeout(() => geoMap.invalidateSize(), 200);
    }

    reverseGeocode(lat, lng).then(address => {
      if (geoAddress) geoAddress.textContent = address || 'Indirizzo non disponibile';
      updateShareLinks(lat, lng, address);
      setGeoStatus('Posizione rilevata. Puoi inviarla subito al nostro team.', 'success');
    });
  }

  function locateUser() {
    if (!navigator.geolocation) {
      setGeoStatus('Il tuo browser non supporta la geolocalizzazione.', 'error');
      return;
    }

    if (geoLocateBtn) {
      geoLocateBtn.disabled = true;
      geoLocateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Rilevamento...';
    }
    setGeoStatus('Stiamo rilevando la tua posizione. Accetta il permesso se richiesto.');

    navigator.geolocation.getCurrentPosition(
      pos => {
        if (geoLocateBtn) {
          geoLocateBtn.disabled = false;
          geoLocateBtn.innerHTML = '<i class="fas fa-location-crosshairs"></i> Aggiorna posizione';
        }
        showPosition(pos.coords.latitude, pos.coords.longitude, pos.coords.accuracy);
      },
      err => {
        if (geoLocateBtn) {
          geoLocateBtn.disabled = false;
          geoLocateBtn.innerHTML = '<i class="fas fa-location-crosshairs"></i> Trova la mia posizione';
        }
        const messages = {
          1: 'Permesso negato. Attiva la posizione nelle impostazioni del browser.',
          2: 'Posizione non disponibile. Riprova tra qualche secondo.',
          3: 'Rilevamento scaduto. Controlla il GPS e riprova.'
        };
        setGeoStatus(messages[err.code] || 'Impossibile rilevare la posizione.', 'error');
      },
      { enableHighAccuracy: true, timeout: 15000, maximumAge: 0 }
    );
  }

  function initGeoMap() {
    if (!geoMapEl || typeof L === 'undefined' || geoMap) return;

    geoMap = L.map(geoMapEl, {
      scrollWheelZoom: false,
      zoomControl: true
    }).setView(BRESCIA_CENTER, 11);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(geoMap);

    L.marker(BRESCIA_CENTER, {
      icon: L.divIcon({
        className: 'geo-marker-base-wrap',
        html: '<span class="geo-marker-base"></span>',
        iconSize: [12, 12],
        iconAnchor: [6, 6]
      })
    }).addTo(geoMap).bindPopup('<strong>Solomon</strong><br>Area operativa Brescia');

    setTimeout(() => geoMap.invalidateSize(), 100);
  }

  if (geoMapEl) {
    initGeoMap();

    if (geoLocateBtn) geoLocateBtn.addEventListener('click', locateUser);

    if (geoCopyBtn) {
      geoCopyBtn.addEventListener('click', async () => {
        if (!currentPosition) return;
        const text = (geoAddress?.textContent || '') + '\n' +
          formatCoords(currentPosition.lat, currentPosition.lng) + '\n' +
          mapsUrl(currentPosition.lat, currentPosition.lng);
        try {
          await navigator.clipboard.writeText(text.trim());
          setGeoStatus('Posizione copiata negli appunti.', 'success');
        } catch {
          setGeoStatus('Copia non riuscita. Usa WhatsApp o Maps.', 'error');
        }
      });
    }

    const geoSection = document.getElementById('posizione');
    if (geoSection && geoMap) {
      const mapObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            setTimeout(() => geoMap.invalidateSize(), 150);
          }
        });
      }, { threshold: 0.2 });
      mapObserver.observe(geoSection);
    }

    if (window.location.hash === '#posizione') {
      setTimeout(() => geoMap?.invalidateSize(), 400);
    }
  }
})();
