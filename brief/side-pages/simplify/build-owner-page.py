# -*- coding: utf-8 -*-
"""Owner page for the SIMPLIFY round. Reads the before/after numbers from verify-before/verify.json and
verify-after/verify.json, embeds the phone renders as JPEG data URIs, and writes the HTML the Artifact tool publishes.
The critique section reads brief/side-pages/simplify/critique/SUMMARY.json when it exists (written after the
critique workflow closes); until then it prints the honest placeholder."""
import base64, io, json, os, re
from PIL import Image
SIM = '/home/user/ElmsNest/brief/side-pages/simplify'
OUT = '/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/simplify-owner.html'
A = json.load(open(f'{SIM}/verify-after/verify.json'))
B = json.load(open(f'{SIM}/verify-before/verify.json'))
CRIT = json.load(open(f'{SIM}/critique/SUMMARY.json')) if os.path.exists(f'{SIM}/critique/SUMMARY.json') else None

def jpg(path, width=390, q=78):
    im = Image.open(path).convert('RGB')
    if im.width > width: im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def shot(dirname, name):
    p = f'{SIM}/{dirname}/{name}'
    return jpg(p) if os.path.exists(p) else ''

PAGES = [('home', 'الرئيسية', 6), ('collection-all', 'كل المنتجات (27)', 8), ('collection-path', 'كولكشن الشباك', 8),
         ('pdp-rope', 'منتج: حبل إضاءة (16 خياراً)', 6), ('pdp-path', 'منتج: مصباح شباك (خيار واحد)', 6), ('pdp-deck', 'منتج: إضاءة درج (4 خيارات)', 6)]
def sc(d, k): return d.get(f'{k}-m-js', {}).get('screens', '—')
rows = ''.join(f'<tr><td>{label}</td><td class="n old">{sc(B,k)}</td><td class="n new">{sc(A,k)}</td><td class="n tgt">≤ {t}</td></tr>' for k, label, t in PAGES)

flow = [('home-m-js-full.png', 'الرئيسية', 'صورة، جملة واحدة، زرّ واحد؛ ثم أربع كولكشنات بأسمائها من المتجر، أربعة منتجات، «متى نعم ومتى لا»، وثلاثة أرقام.'),
        ('collection-all-m-js-full.png', 'كل المنتجات', 'شبكة Kalles الأصلية ببطاقاتها، صورة المنتج الأصلية في كل بطاقة، صفّ أزرار للكولكشنات الأربع، وترتيب واحد.'),
        ('pdp-rope-m-js-full.png', 'صفحة المنتج', 'معرض الصور الأصلي، الاسم، السعر وسعر المتر، الخيارات كأزرار، زرّ شراء واحد وشريط لاصق ثانٍ متزامن معه، سطر شروط واحد، وسطر «لا يناسب» ثم رابط البريد.')]
flow_html = ''.join(f'<figure><img src="{shot("verify-after", f)}" alt="" loading="lazy"><figcaption><b>{t}</b>{d}</figcaption></figure>' for f, t, d in flow)
drawer = shot('verify-after', 'drawer-rope-mobile.png')
drawer_html = f'<figure class="drawer"><img src="{drawer}" alt="" loading="lazy"><figcaption><b>الدرج بعد الإضافة</b>درج Kalles نفسه بالغلاف الليلي — وهذا هو موضوع جولة السلة التالية (سلّتا الحذف، مجموع السطر، سطر الشروط).</figcaption></figure>' if drawer else ''

ba = [('home', 'الرئيسية'), ('collection-all', 'كل المنتجات')]
ba_html = ''.join(f'<div class="pair"><figure class="old"><img src="{shot("verify-before", k + "-m-js-full.png")}" alt="" loading="lazy"><figcaption><b>قبل</b>{sc(B,k)} شاشة</figcaption></figure><figure class="new"><img src="{shot("verify-after", k + "-m-js-full.png")}" alt="" loading="lazy"><figcaption><b>بعد</b>{sc(A,k)} شاشة</figcaption></figure><h3>{t}</h3></div>' for k, t in ba)

if CRIT:
    crit_html = CRIT['html']
else:
    crit_html = '<p class="muted">النقد العدائي يعمل الآن على اللقطات الحقيقية بأربع عدسات — مشترٍ لأول مرة، مهندس اختبار، حارس الصدق، وشكاواك الثلاث بحروفها — ومشكّك على كل ملاحظة. تُضاف نتيجته هنا عند إغلاقه.</p>'

html = f'''<title>التبسيط</title>
<meta name="description" content="الصفحات الثلاث بعد حكمك: الليلي الداكن مبسّطاً على قوالب Kalles الأصلية — الأرقام قبل وبعد، رحلة الهاتف كاملة، وما بقي لك في لوحة الإدارة.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=IBM+Plex+Sans+Arabic:wght@300;400;500;600&display=swap">
<style>
:root{{--bg:#070b13;--bg2:#0d1524;--ink:#f4eee3;--ink2:#c9c4b8;--mute:#8f95a3;--gold:#e9b96e;--glow:#ffd394;--hair:rgba(244,238,227,.13);--bad:#f0a0a0;--ok:#8fd3a5;
--serif:"Amiri",serif;--sans:"IBM Plex Sans Arabic",system-ui,-apple-system,"Segoe UI",sans-serif}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-weight:300;font-size:16px;line-height:1.75;direction:rtl;-webkit-font-smoothing:antialiased}}
.wrap{{width:min(1140px,100% - 44px);margin-inline:auto}}
h1,h2,h3{{font-family:var(--serif);font-weight:700;line-height:1.15;margin:0;text-wrap:balance}}
h1{{font-size:clamp(36px,5.6vw,64px)}} h2{{font-size:clamp(26px,3.2vw,40px);margin-bottom:12px}} h3{{font-size:22px}}
p{{margin:0 0 13px;max-width:74ch}} .muted{{color:var(--mute)}}
.eyebrow{{display:flex;align-items:center;gap:13px;font-size:12px;font-weight:500;letter-spacing:.14em;color:var(--gold);margin-bottom:13px}}
.eyebrow::before{{content:"";width:36px;height:1px;background:var(--gold);flex:none}}
header.top{{padding:66px 0 40px;position:relative;overflow:hidden}}
header.top::after{{content:"";position:absolute;inset-inline-start:-8%;top:-45%;width:66%;height:150%;background:radial-gradient(closest-side,rgba(255,211,148,.10),transparent 70%);pointer-events:none}}
.lede{{font-size:19.5px;color:var(--ink2);max-width:58ch;margin-top:18px;position:relative}}
blockquote{{margin:18px 0 0;padding-inline-start:18px;border-inline-start:2px solid var(--gold);font-family:var(--serif);font-size:20px;line-height:1.6;color:var(--ink);max-width:60ch}}
blockquote small{{display:block;font-family:var(--sans);font-size:13px;color:var(--mute);margin-top:6px}}
nav.toc{{position:sticky;top:0;z-index:9;background:rgba(7,11,19,.94);backdrop-filter:blur(10px);border-block:1px solid var(--hair);padding:11px 0}}
nav.toc ul{{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:2px 22px;font-size:14px}}
nav.toc a{{color:var(--ink2);text-decoration:none;padding:5px 0;border-bottom:1px solid transparent}}
nav.toc a:hover,nav.toc a:focus-visible{{color:var(--glow);border-color:var(--glow)}}
section{{padding:58px 0 26px;scroll-margin-top:62px}} section+section{{border-top:1px solid var(--hair)}}
table{{border-collapse:collapse;width:100%;margin-top:22px;font-variant-numeric:tabular-nums}}
th,td{{text-align:start;padding:12px 10px;border-bottom:1px solid var(--hair);vertical-align:top}}
th{{font-weight:500;font-size:13px;color:var(--mute);letter-spacing:.04em}}
td.n{{font-family:var(--serif);font-size:24px;line-height:1;white-space:nowrap}} td.old{{color:var(--mute)}} td.new{{color:var(--glow)}} td.tgt{{color:var(--ink2);font-size:16px;font-family:var(--sans)}}
.flow{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:26px;margin-top:26px;align-items:start}}
.flow figure,.pair figure{{margin:0}} .flow img,.pair img{{width:100%;display:block;border:1px solid var(--hair)}}
figcaption{{margin-top:10px;font-size:14px;color:var(--ink2)}} figcaption b{{display:block;font-family:var(--serif);font-size:19px;color:var(--ink);margin-bottom:3px}}
.pair{{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:26px;align-items:start}} .pair h3{{grid-column:1/-1;order:-1}}
.pair .old img{{filter:saturate(.7) brightness(.85)}} .pair .old b{{color:var(--mute)}}
ul.list{{margin:14px 0 0;padding:0;list-style:none}} ul.list li{{padding:12px 0;border-top:1px solid var(--hair);max-width:74ch}} ul.list li b{{color:var(--ink);font-weight:500}}
.rules li{{color:var(--ink2)}}
.admin li{{display:grid;grid-template-columns:auto 1fr;gap:14px;align-items:baseline}} .admin li::before{{content:"☐";font-size:18px;color:var(--gold)}}
footer{{padding:40px 0 60px;color:var(--mute);font-size:13px;border-top:1px solid var(--hair)}}
@media (max-width:700px){{.pair{{grid-template-columns:1fr 1fr;gap:10px}} td.n{{font-size:20px}} .lede{{font-size:17px}}}}
</style>
<header class="top"><div class="wrap">
<p class="eyebrow">ElmsNest · ثيم التطوير 154726400174 · غير منشور</p>
<h1>التبسيط</h1>
<p class="lede">الصفحات الثلاث بعد حكمك في اليوم نفسه: النظرة الليلية بقيت، والتعقيد ذهب. الرئيسية من عشر شاشات إلى خمس، الكتالوج من ستٍّ وعشرين إلى ثمانٍ، صفحة المنتج من عشر إلى أربع — على قوالب Kalles الأصلية التي يعرفها كل مشترٍ، بصورة المنتج الأصلية في كل مكان.</p>
<blockquote>«صممتها تصميم بصري جميل جداً لكنه معقد ومش زابط للمتجر… هدفي كان نعطي افضل تصميم بصري لكن يكون بسيط للعميل»<small>حكمك، 2026-09-05 — وهو الموجز الذي بُنيت عليه هذه الجولة كلها</small></blockquote>
</div></header>
<nav class="toc"><div class="wrap"><ul><li><a href="#numbers">الأرقام</a></li><li><a href="#flow">رحلة الهاتف</a></li><li><a href="#ba">قبل وبعد</a></li><li><a href="#answers">أجوبتك الخمسة</a></li><li><a href="#critique">النقد</a></li><li><a href="#admin">ما بقي لك</a></li><li><a href="#process">كيف جرى</a></li></ul></div></nav>

<section id="numbers"><div class="wrap">
<p class="eyebrow">القياس</p><h2>كم شاشة هاتف تحتاج كل صفحة</h2>
<p>مقيسة على هاتف 390×844 بجافاسكربت، الفوتر محسوب. «قبل» هي الصفحات المرفوضة كما كانت على ثيم التطوير صباح اليوم؛ «الهدف» من مواصفة التبسيط.</p>
<div style="overflow-x:auto"><table><thead><tr><th>الصفحة</th><th>قبل</th><th>بعد</th><th>الهدف</th></tr></thead><tbody>{rows}</tbody></table></div>
<ul class="list rules"><li><b>صفر</b> لوحات مرسومة بدل الصور، صفر أخطاء Liquid، صفر واتساب، صفر فيض أفقي — على الصفحات الست وعلى ثلاثة أحجام شاشة، بجافاسكربت وبدونها.</li>
<li><b>27 من 27</b> بطاقة في «كل المنتجات» تعرض صورة المنتج الأصلية كما هي في المتجر (فُحصت على HTML المتجر الحي).</li>
<li><b>نموذج شراء واحد</b> وشريط لاصق واحد وحقل كمية واحد في كل صفحة منتج، ومختار خيارات يعمل بلا جافاسكربت.</li>
<li><b>الإضافة إلى السلة</b> جُرِّبت على المتجر الحي: المنتج وصل إلى الدرج بالخيار المختار.</li></ul>
</div></section>

<section id="flow"><div class="wrap">
<p class="eyebrow">الرحلة</p><h2>من الرئيسية إلى الدرج، على هاتف</h2>
<div class="flow">{flow_html}{drawer_html}</div>
</div></section>

<section id="ba"><div class="wrap">
<p class="eyebrow">المقارنة</p><h2>الصفحة نفسها، قبل وبعد</h2>
{ba_html}
</div></section>

<section id="answers"><div class="wrap">
<p class="eyebrow">ما قلتَه</p><h2>أجوبتك الخمسة، وكيف نُفّذت</h2>
<ul class="list">
<li><b>«النظرة الليلية الداكنة بس مبسّطة»</b> — الأرض الليلية والذهب والخطّان بقيا؛ المصابيح التي تُضاء عند الوصول، والمساطر، والشرائط المكرّرة، ذهبت. كل فعل (تصفّح، اختيار، كمية، شراء) بمكوّن Kalles الأصلي.</li>
<li><b>«الصورة الأصلية في كل مكان»</b> — البطاقات والمعرض يعرضان صور المتجر بترتيبها، بلا استبدال ولا رسوم. (خمسة منتجات صورتها الأولى ملصق مكتوب — ورقة إعادة الترتيب مهمة منفصلة تنتظر موافقتك.)</li>
<li><b>«فش رقم واتس، خلّي البريد»</b> — وعد «ابعتلنا صورة للمكان» مرة واحدة في كل صفحة عبر البريد، ومرة في الفوتر؛ كلمة واتساب لا تظهر في أي مكان، حتى في تسميات المحرّر.</li>
<li><b>«هيك» على أسماء الكولكشنات</b> — أسماء Shopify كما هي، كلمة المكان سطراً صغيراً حيث تحمل معنى، الكولكشنات الأربع هي المدخل، «كل المنتجات» شبكة عادية، وترتيب واحد في القائمة والبلاطات والفلتر والفوتر.</li>
<li><b>«بنقدر نصغّره»</b> — بانر الكوكيز إعداد في لوحة الإدارة (أدناه).</li>
</ul>
</div></section>

<section id="critique"><div class="wrap">
<p class="eyebrow">النقد العدائي</p><h2>ما وجده النقد على اللقطات الحقيقية</h2>
{crit_html}
</div></section>

<section id="admin"><div class="wrap">
<p class="eyebrow">خارج الكود</p><h2>ما بقي لك في لوحة الإدارة</h2>
<ul class="list admin">
<li><b>بانر الكوكيز</b> — Settings ← Customer privacy ← Cookie banner: الوضع المضغوط أسفل الشاشة، وألوانه.</li>
<li><b>القائمة الرئيسية</b> — عنصر «קולקציות» يشير إلى /collections (صفحة القائمة الكريمية القديمة)؛ وجّهه إلى /collections/all. القوائم مشتركة مع الثيم الحي، فهي قرارك.</li>
<li><b>صور المنتجات</b> — خمسة منتجات لها لقطة نظيفة في موضع لاحق يُستحسن نقلها إلى الموضع الأول، وأربعة عشر لا لقطة نظيفة لها. ورقة بالأسماء والمواضع تنتظر موافقتك قبل أي تغيير.</li>
<li><b>سعر المقارنة</b> على إضاءة الدرج (199.90) — احذفه من لوحة الإدارة؛ الغلاف يخفيه، لكن الأصل أن لا يوجد.</li>
</ul>
</div></section>

<section id="process"><div class="wrap">
<p class="eyebrow">الأمانة</p><h2>كيف جرى العمل، بما فيه ما أخطأتُ فيه</h2>
<ul class="list">
<li><b>جلستان.</b> حكمك وصل إلى جلسة أخرى بنت هذه الجولة وتوقفت لأن جلستي كانت مفتوحة على جولة السلة. دمجتُ عملها، وأكملتُ ما سلّمته: مراجعة، نشر، تحقق، نقد.</li>
<li><b>المراجعة.</b> ستة مراجعين قرأوا الملفات الاثنين والعشرين سطراً سطراً (27 ملاحظة، واحدة كبيرة: أرقام لاتينية كانت تنقلب في سطر عبري)، ومشكّك على كل ملاحظة نقض واحدة، ومصلح طبّق الباقي، ومراجع ثانٍ فحص ما تغيّر.</li>
<li><b>النشر.</b> أربع قواعد في Shopify لم تكن معروفة أوقفت أربعة ملفات مرة واحدة كلٌّ، فأُصلحت وأُعيد إرسالها؛ الملفات كلها على الثيم وبصماتها مطابقة.</li>
<li><b>القياس.</b> ثلاث قراءات في أداة التحقق كانت خطأ الأداة لا الصفحة (إعادة تسمية الملفات في المرآة، أزرار مخفية خلف تسميات، نص الوصف الخام)؛ صُحّحت الأداة ووُثّقت الاستثناءات. و«كل المنتجات» قِيست 8.15 ثم 8.02 ثم 7.94 عبر ثلاث رافعات من إعدادات Kalles نفسها.</li>
<li><b>خطآن سجّلتهما على نفسي.</b> رسالة إيداع قالت إن الأرقام حُفظت ولم تكن قد حُفظت (أداة التصحيح توقفت قبل الكتابة) — صُحّح في الإيداع التالي بنصّه. وفي الصباح، قبل حكمك، أصلحتُ زرّ الرئيسية الذي كان يُكتب بحبر لا يُقرأ (1.21:1 ← 13.24:1) رغم أن حكمك على الرئيسية كان معلّقاً، لأن زرّاً لا يُقرأ يُفسد الحكم نفسه.</li>
<li><b>ما لم يُقَس.</b> تبديل السعر عند الضغط على خيار هو جافاسكربت Kalles الأصلية التي تطلب الصفحة من الخادم؛ المرآة لا تستطيع طلبها، فأثبتُّ نصف الخادم على المتجر الحي (الخيار الثاني يُعرض بسعره ورقمه) ونصف الإضافة إلى السلة، وتركتُ النصف الثالث لعينك على المعاينة.</li>
</ul>
</div></section>
<footer><div class="wrap">ElmsNest · جولة التبسيط · 2026-09-05 · المعاينة: <span dir="ltr">elmsnest.com/?preview_theme_id=154726400174</span> — لم يُنشر شيء على المتجر الحي.</div></footer>
'''
open(OUT, 'w', encoding='utf-8').write(html)
print('written', OUT, f'{os.path.getsize(OUT)/1e6:.1f} MB', '| critique section:', 'real' if CRIT else 'placeholder')
