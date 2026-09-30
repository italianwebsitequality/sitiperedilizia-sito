#!/usr/bin/env python3
"""Genera le 4 demo /demo/<slug>/index.html da un unico modello con temi diversi.
Le immagini vengono da img/d-<slug>-<nome>-{S,L}.webp (vedi build-img.sh)."""
import os, html
ROOT = os.path.join(os.path.dirname(__file__), "..")

DEMOS = {
 "serramenti": dict(
  nome="Bergamini Serramenti", tag="Serramenti e infissi su misura · Lecco", citta="Lecco",
  fonts="Fraunces:opsz,wght@9..144,500;9..144,700|Inter:wght@400;500;600",
  fd="'Fraunces',Georgia,serif", fb="'Inter',system-ui,sans-serif",
  bg="#F4F3F0", ink="#1D2023", acc="#B5762F", dark="#23272B", layout="full", upper=False,
  h1="Finestre che durano una vita. Su misura, posate a regola d'arte.",
  sub="Progettiamo, produciamo e installiamo serramenti in legno, alluminio e legno-alluminio per case nuove e ristrutturazioni tra Lecco e il lago.",
  cifre=[("40+","anni di bottega"),("100%","produzione propria"),("10 anni","garanzia sui serramenti")],
  servizi=[("Legno e legno-alluminio","Rovere, larice e abete lavorati in laboratorio, finiture a olio o verniciate."),("Alluminio a taglio termico","Profili sottili, grandi vetrate, massima tenuta per le case moderne."),("Sostituzione e detrazioni","Sostituiamo i vecchi infissi senza rovinare intonaci e cornici, con pratiche per le detrazioni."),("Persiane e oscuranti","Persiane, scuri e tapparelle coordinati al serramento.")],
  foto=["hero","posa","dettaglio","showroom","finito","laboratorio"], cap=["Il laboratorio","La posa","Il dettaglio","Lo showroom","Il risultato","La produzione"],
  passi=[("Sopralluogo","Misuriamo e ascoltiamo cosa serve alla casa."),("Preventivo scritto","Materiali, finiture e tempi indicati per iscritto."),("Produzione","Costruiti nel nostro laboratorio."),("Posa e collaudo","Installazione pulita e controllo finale insieme.")]),
 "tetti": dict(
  nome="Colombo Coperture", tag="Tetti, isolamento e lattoneria · Como e Lecco", citta="Como e Lecco",
  fonts="Bebas+Neue|DM+Sans:wght@400;500;700",
  fd="'Bebas Neue',Impact,sans-serif", fb="'DM Sans',system-ui,sans-serif",
  bg="#FAF6F1", ink="#2A2320", acc="#C4451C", dark="#2F3A44", layout="split", upper=True,
  h1="Il tetto giusto. Una volta sola.",
  sub="Rifacimento, manutenzione e isolamento di coperture: lavoriamo in quota, in sicurezza, con cantieri puliti e tempi rispettati.",
  cifre=[("1.200+","tetti eseguiti"),("24 h","sopralluogo gratuito"),("Ponteggi","a norma, sempre")],
  servizi=[("Rifacimento coperture","Rimozione, nuova struttura e manto in tegole, coppi o lamiera."),("Isolamento e ventilazione","Meno dispersioni, più comfort e bonus fiscali dove previsti."),("Lattoneria in rame","Grondaie, pluviali e scossaline su misura, che durano."),("Manutenzione e riparazioni","Infiltrazioni, tegole rotte, pulizia: interveniamo anche in urgenza.")],
  foto=["hero","tegole","isolamento","gronda","dopo","drone"], cap=["In quota","Le tegole","L'isolamento","La lattoneria","Dopo il lavoro","Dall'alto"],
  passi=[("Sopralluogo","Saliamo sul tetto e controlliamo lo stato reale."),("Preventivo scritto","Voci chiare, senza sorprese a lavori iniziati."),("Cantiere","Ponteggi, squadra fissa, cantiere ordinato."),("Consegna","Controllo finale con foto del lavoro.")]),
 "impianti": dict(
  nome="Rota Termoidraulica", tag="Caldaie, pompe di calore e bagni · Brianza", citta="Brianza",
  fonts="Space+Grotesk:wght@500;700|Source+Sans+3:wght@400;600",
  fd="'Space Grotesk',system-ui,sans-serif", fb="'Source Sans 3',system-ui,sans-serif",
  bg="#F1F5F5", ink="#0F2A33", acc="#B8632B", dark="#0F3B47", layout="full", upper=False,
  h1="Caldo d'inverno, fresco d'estate. Consumi più bassi.",
  sub="Installiamo e manuteniamo caldaie a condensazione, pompe di calore e impianti idraulici per case, condomini e ristrutturazioni.",
  cifre=[("30+","anni di esperienza"),("Pronto","intervento in giornata"),("Pratiche","detrazioni incluse")],
  servizi=[("Caldaie e pompe di calore","Sostituzione della vecchia caldaia con sistemi efficienti."),("Riscaldamento a pavimento","Posa di impianti radianti in nuove costruzioni e ristrutturazioni."),("Bagni chiavi in mano","Impianto idraulico, sanitari e doccia: un solo referente."),("Manutenzione e pronto intervento","Contratti annuali e uscite rapide per guasti e perdite.")],
  foto=["hero","caldaia","tubi","bagno","pavimento","furgone"], cap=["L'installazione","La caldaia","I collettori","Il bagno","Il radiante","Il furgone"],
  passi=[("Sopralluogo","Verifichiamo impianto esistente e consumi."),("Preventivo scritto","Soluzione consigliata, costi e incentivi disponibili."),("Installazione","Squadra qualificata, lavoro pulito, poche ore di disagio."),("Collaudo","Test, dichiarazione di conformità e libretto.")]),
 "imbiancatura": dict(
  nome="Sala Decorazioni", tag="Imbiancatura, stucchi e cartongesso · Lecco", citta="Lecco",
  fonts="Playfair+Display:wght@500;700|Nunito+Sans:wght@400;600",
  fd="'Playfair Display',Georgia,serif", fb="'Nunito Sans',system-ui,sans-serif",
  bg="#F6F4EE", ink="#2B2A26", acc="#5E7A5A", dark="#33382F", layout="split", upper=False,
  h1="Pareti che si notano. Finiture che restano.",
  sub="Tinteggiature, stucchi veneziani, cartongesso e ripristino di facciate: precisione da artigiani, pulizia da professionisti.",
  cifre=[("15+","anni di mestiere"),("Case pulite","copriamo e ripuliamo tutto"),("Colori","consulenza inclusa")],
  servizi=[("Imbiancatura interni","Pareti e soffitti impeccabili, con prodotti a basso odore."),("Stucchi e finiture decorative","Calce, stucco veneziano, effetti materici."),("Cartongesso","Pareti, controsoffitti e nicchie su misura."),("Facciate e esterni","Ripristino e tinteggiatura con piattaforme e ponteggi.")],
  foto=["hero","stucco","campioni","cartongesso","dopo","facciata"], cap=["Al lavoro","Lo stucco","I colori","Il cartongesso","Il risultato","La facciata"],
  passi=[("Sopralluogo","Guardiamo le pareti, scegliamo insieme i colori."),("Preventivo scritto","Superfici, prodotti e tempi indicati."),("Lavoro","Protezioni, stesure, controllo di ogni mano."),("Consegna","Pulizia completa e ritocchi inclusi.")]),
}

T = """<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,follow">
<title>{nome} | {tag}</title>
<meta name="description" content="{sub}">
<script>document.documentElement.classList.add('js');if(/[?&]mock\\b/.test(location.search))document.documentElement.classList.add('mock')</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={fam}&display=swap" rel="stylesheet">
<style>
:root{{--bg:{bg};--ink:{ink};--acc:{acc};--dk:{dark};--fd:{fd};--fb:{fb};--pad:clamp(20px,4.4vw,64px)}}
*{{box-sizing:border-box;margin:0;padding:0}}html{{scroll-behavior:smooth;scroll-padding-top:70px}}
body{{font:400 17px/1.6 var(--fb);color:var(--ink);background:var(--bg);-webkit-font-smoothing:antialiased;overflow-x:hidden}}
img{{display:block;max-width:100%;height:auto}}a{{color:inherit}}ul{{list-style:none}}
.w{{max-width:1300px;margin:0 auto;padding:0 var(--pad)}}
h1,h2,h3{{font-family:var(--fd);line-height:1.02;{up}}}
h2{{font-size:clamp(34px,5vw,68px);max-width:16ch}}
.lab{{font-size:13px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--acc);margin-bottom:14px}}
.btn{{display:inline-block;background:var(--acc);color:#fff;text-decoration:none;font-weight:600;padding:16px 26px;transition:transform .25s}}.btn:hover{{transform:translateY(-2px)}}
.btn.o{{background:transparent;color:inherit;box-shadow:inset 0 0 0 1.5px currentColor}}
header{{position:fixed;inset:0 0 auto 0;z-index:20;transition:background .3s;color:#fff}}header.s{{background:var(--bg);color:var(--ink);border-bottom:1px solid rgba(0,0,0,.1)}}
.nav{{display:flex;align-items:center;justify-content:space-between;height:70px}}
.logo{{font:700 24px var(--fd);text-decoration:none;{up}}}
.nav nav{{display:flex;gap:26px;align-items:center}}.nav nav a{{text-decoration:none;font-size:15px;font-weight:500}}.nav nav .btn{{padding:11px 18px;color:#fff}}
@media(max-width:760px){{.nav nav a:not(.btn){{display:none}}}}
.hero{{position:relative;min-height:100svh;display:flex;align-items:flex-end;color:#fff;background:var(--dk)}}
.hero picture,.hero img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.hero:before{{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,.05) 35%,rgba(0,0,0,.78))}}
.hero .w{{position:relative;z-index:2;padding-bottom:64px;width:100%}}
.hero h1{{font-size:clamp(42px,7.4vw,112px);max-width:15ch;margin:14px 0 20px}}.hero p{{max-width:48ch;font-size:19px;opacity:.92}}
.hero .cta{{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}}.hero .btn.o{{color:#fff}}
.split .hero{{align-items:stretch;padding-top:70px}}
@media(min-width:900px){{.split .hero{{display:grid;grid-template-columns:1fr 1fr;background:var(--bg);color:var(--ink)}}
.split .hero picture{{position:relative;grid-column:2;grid-row:1;min-height:100%}}.split .hero:before{{display:none}}
.split header:not(.s){{color:var(--ink)}}.split .hero .w{{grid-column:1;grid-row:1;align-self:center;padding:60px var(--pad);max-width:none}}.split .hero .btn.o{{color:var(--ink)}}}}
.strip{{background:var(--ink);color:var(--bg)}}.strip .w{{display:grid;grid-template-columns:repeat(3,1fr);gap:0}}
.strip div{{padding:30px 20px 30px 0}}.strip div+div{{padding-left:24px;border-left:1px solid rgba(255,255,255,.18)}}
.strip b{{display:block;font:700 clamp(30px,4vw,52px)/1 var(--fd);color:var(--acc)}}.strip span{{font-size:14px;opacity:.8}}
section{{padding:clamp(64px,9vw,130px) 0}}
.serv{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));margin-top:44px;border-top:2px solid var(--ink)}}
.serv div{{padding:28px 24px 34px 0;border-bottom:1px solid rgba(0,0,0,.12)}}.serv i{{font:700 15px var(--fd);color:var(--acc);font-style:normal}}
.serv h3{{font-size:26px;margin:12px 0 10px}}.serv p{{opacity:.72;max-width:34ch}}
.gal{{display:grid;grid-template-columns:repeat(12,1fr);gap:12px;margin-top:44px}}
.gal figure{{position:relative;overflow:hidden;background:var(--dk)}}.gal img{{width:100%;height:100%;object-fit:cover;transition:transform .8s}}.gal figure:hover img{{transform:scale(1.05)}}
.gal figcaption{{position:absolute;left:14px;bottom:12px;color:#fff;font-size:13px;font-weight:600;letter-spacing:.06em;text-shadow:0 1px 10px rgba(0,0,0,.7)}}
.g1{{grid-column:span 7;aspect-ratio:7/5}}.g2{{grid-column:span 5}}.g3{{grid-column:span 4;aspect-ratio:1}}.g4{{grid-column:span 4;aspect-ratio:1}}.g5{{grid-column:span 4;aspect-ratio:1}}
.dark{{background:var(--dk);color:#fff}}.dark .lab{{color:#fff;opacity:.7}}
.steps{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:34px;margin-top:44px}}
.steps div{{border-top:2px solid var(--acc);padding-top:18px}}.steps h3{{font-size:26px;margin-bottom:8px}}.steps p{{opacity:.75}}
.contatti .g{{display:grid;grid-template-columns:1fr 1fr;gap:56px}}
.contatti dl div{{padding:18px 0;border-top:1px solid rgba(0,0,0,.14)}}.contatti dt{{font-size:13px;letter-spacing:.14em;text-transform:uppercase;opacity:.6}}.contatti dd{{font:600 22px var(--fd)}}
.contatti a{{text-decoration:none;border-bottom:2px solid var(--acc)}}
footer{{padding:26px 0 90px;font-size:14px;opacity:.65;border-top:1px solid rgba(0,0,0,.1)}}
.bar{{display:none}}
@media(max-width:760px){{.contatti .g{{grid-template-columns:1fr}}.g1,.g2{{grid-column:span 12;aspect-ratio:4/3}}.g3,.g4{{grid-column:span 6}}.g5{{grid-column:span 12;aspect-ratio:2/1}}
.bar{{display:grid;grid-template-columns:1fr 1fr;position:fixed;inset:auto 0 0 0;z-index:30}}.bar a{{padding:16px;text-align:center;color:#fff;font-weight:600;text-decoration:none;background:var(--acc)}}.bar a+a{{background:var(--ink)}}
.strip .w{{grid-template-columns:1fr}}.strip div+div{{padding-left:0;border-left:0;border-top:1px solid rgba(255,255,255,.18)}}}}
.js .rv{{opacity:0;transform:translateY(26px);transition:opacity .8s,transform .8s}}.js .rv.in,.mock .rv{{opacity:1!important;transform:none!important;transition:none}}
</style></head><body class="{layout}">
<header id="hd"><div class="w nav"><a class="logo" href="#">{nome}</a><nav><a href="#servizi">Servizi</a><a href="#lavori">Lavori</a><a href="#contatti">Contatti</a><a class="btn" href="#contatti">Preventivo</a></nav></div></header>
<div class="hero"><picture><img src="/img/d-{slug}-hero-L.webp" srcset="/img/d-{slug}-hero-S.webp 800w,/img/d-{slug}-hero-L.webp 1600w" sizes="100vw" alt="" fetchpriority="high"></picture>
<div class="w"><div class="lab" style="color:inherit;opacity:.85">{tag}</div><h1>{h1}</h1><p>{sub}</p><div class="cta"><a class="btn" href="#contatti">Chiedi un preventivo</a><a class="btn o" href="tel:+390000000000">Chiama ora</a></div></div></div>
<div class="strip"><div class="w">{cifre}</div></div>
<section id="servizi"><div class="w"><div class="lab rv">Cosa facciamo</div><h2 class="rv">{h2s}</h2><div class="serv">{servizi}</div></div></section>
<section id="lavori" style="padding-top:0"><div class="w"><div class="lab rv">Lavori realizzati</div><h2 class="rv">Guardate prima di chiamarci.</h2>
<div class="gal">{gal}</div></div></section>
<section class="dark"><div class="w"><div class="lab">Come lavoriamo</div><h2>Dal sopralluogo alla consegna.</h2><div class="steps">{passi}</div></div></section>
<section class="contatti" id="contatti"><div class="w"><div class="g"><div><div class="lab">Contatti</div><h2>Raccontateci il lavoro.</h2><p style="margin-top:18px;opacity:.75;max-width:40ch">Un sopralluogo gratuito e un preventivo scritto, senza impegno. Zona: {citta} e dintorni.</p></div>
<dl><div><dt>Telefono</dt><dd><a href="tel:+390000000000">+39 000 000 0000</a></dd></div><div><dt>WhatsApp</dt><dd><a href="https://wa.me/390000000000">Scrivi all'ufficio</a></dd></div><div><dt>Email</dt><dd><a href="mailto:info@example.it">info@example.it</a></dd></div></dl></div></div></section>
<footer><div class="w">{nome} · Sito dimostrativo realizzato da sitiperedilizia.it: nomi, foto e recapiti sono d'esempio.</div></footer>
<div class="bar"><a href="tel:+390000000000">Chiama</a><a href="#contatti">Preventivo</a></div>
<script>var h=document.getElementById('hd');function f(){{h.classList.toggle('s',scrollY>40)}}addEventListener('scroll',f,{{passive:true}});f();
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.12}});document.querySelectorAll('.rv').forEach(function(e){{io.observe(e)}});</script>
</body></html>"""

for slug, d in DEMOS.items():
    e = html.escape
    cifre = "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in d["cifre"])
    servizi = "".join(f"<div><i>0{i+1}</i><h3>{e(a)}</h3><p>{e(b)}</p></div>" for i, (a, b) in enumerate(d["servizi"]))
    gal = "".join(
        f'<figure class="g{i+1} rv"><img src="/img/d-{slug}-{n}-L.webp" srcset="/img/d-{slug}-{n}-S.webp 800w,/img/d-{slug}-{n}-L.webp 1600w" sizes="(max-width:760px) 100vw,60vw" alt="{e(c)}" loading="lazy"><figcaption>{e(c)}</figcaption></figure>'
        for i, (n, c) in enumerate(zip(d["foto"][1:], d["cap"][1:])))
    passi = "".join(f"<div><h3>0{i+1} {e(a)}</h3><p>{e(b)}</p></div>" for i, (a, b) in enumerate(d["passi"]))
    out = T.format(slug=slug, fam=d["fonts"].replace("|", "&family="), up="text-transform:uppercase;" if d["upper"] else "",
                   h2s="Il lavoro fatto bene, dall'inizio alla fine.", cifre=cifre, servizi=servizi, gal=gal, passi=passi,
                   **{k: (e(v) if k in ("nome", "tag", "sub", "h1", "citta") else v) for k, v in d.items() if k not in ("cifre", "servizi", "foto", "cap", "passi", "fonts", "upper")})
    p = os.path.join(ROOT, "demo", slug); os.makedirs(p, exist_ok=True)
    open(os.path.join(p, "index.html"), "w").write(out)
    print("ok", slug)
