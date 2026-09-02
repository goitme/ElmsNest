# -*- coding: utf-8 -*-
import base64,os
IMG='/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/report-img'
OUT='/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/side-pages-plan.html'
def img(key,vp):
    p=f'{IMG}/{key}-{vp}.jpg'
    return 'data:image/jpeg;base64,'+base64.b64encode(open(p,'rb').read()).decode()
pages=[
 ('home','الصفحة الرئيسية الجديدة (المرجع)','/','on','على النظام: تدرّج السماء، مصابيح تُضاء عند الوصول، Frank Ruhl Libre، أسعار متوهجة، رأس صفحة مقروء. هذا هو المستوى المطلوب لكل ما يلي.'),
 ('coll-all','كولكشن — كل المنتجات','/collections/all','off','قالب Kalles الافتراضي: أرضية كريمية، شريط بنّي، شريط أدوات بستة أيقونات شبكة وفلتر إنجليزي («Price»)، بطاقات بيضاء، 12 منتجاً بالصفحة، ثلثا الصور الرئيسية ملصقات تسويقية بنص عبري مطبوع. القائمة العلوية غير مرئية.'),
 ('coll-wall','كولكشن — تاورات كير (تאורת קיר)','/collections/solar-wall-lights','off','الشاشة الأولى لا تُظهر سعراً ولا زر شراء على أي جهاز: لافتة + فقرة + شريط أدوات فقط. ستة منتجات كلها متعددة الخيارات، فكل «إضافة سريعة» تفتح نافذة Kalles الكريمية.'),
 ('coll-list','قائمة الكولكشنات','/collections','off','أربع صور مربعة بلوحات تسمية كريمية، 3+1 يتيمة، فتات خبز مكسور «בית ›». الصفحة الرئيسية الجديدة تؤدي هذه الوظيفة أصلاً (قسم «ארבעה מקומות»).'),
 ('pdp-single','صفحة المنتج — خيار واحد','/products/stainless-steel-solar-path-light-ip65','pdp','مرّت بجولة «PDP Design v2»: عشرة أقسام مخصصة، ≈9,500px. كريمية/بنية، صناديق في كل مكان، نحو 5,000px من نصوص قالبية تتكرر على كل منتج، جدول مقارنة ضد «מנורה גנרית זולה»، منتقي خيارات لا يعرض سعراً، وكتل بيانات فارغة (المواصفات/لا يناسب/الأسئلة موجودة لمنتج واحد من 27).'),
 ('pdp-multi','صفحة المنتج — 24 خياراً','/products/solar-crystal-ball-string-lights','pdp','6 أطوال × 4 ألوان: صفوف من المستطيلات بلا سعر لكل طول، السعر المعروض هو سعر أول خيار فقط، وصورة التركيب شريحة كتالوج بيضاء على شاشة سوداء.'),
 ('cart-full','السلة — فيها منتجات','/cart','off','جدول Kalles كريمي بأربعة أعمدة، زر «תשלום» بنّي صغير تحت طيّة الجوال (≈920px) وغير مثبّت، ثم ثلاثة صناديق إرشاد (قسم مخصص صادق النص). درج السلة نفسه يُحقن بـJS ولم يُلتقط بعد — وهو كريمي وسيظهر فوق كل صفحة ليلية.'),
 ('cart-empty','السلة — فارغة','/cart','off','نص Kalles الافتراضي («העגלה שלך ריקה… בדף "חנות" שלנו») وأيقونة رمادية، وصناديق «לפני שממשיכים לתשלום» تظهر حتى والسلة فارغة.'),
 ('search-hits','نتائج البحث (שביל → 13 نتيجة)','/search?q=שביל','off','شريط رمادي فارغ 100px حيث يجب أن يظهر السؤال والعدد (العنوان sr-only)، شريط أدوات كامل لثلاث عشرة نتيجة، نفس بطاقات الكولكشن، شارة «%25-» مقلوبة.'),
 ('search-none','بحث بلا نتائج','/search?q=zzqqxx','off','صندوق تحذير بحدود ونص افتراضي، ولا يوجد حقل بحث لإعادة المحاولة.'),
 ('p404','404 (وأيضاً /collections/sale وصفحة إتاحة الوصول)','/this-page-does-not-exist','off','فراغ كريمي 60vh، عنوان عبري بتباعد أحرف 8px كأنه شعار لاتيني، مخرج وحيد «חזרה ל- דף הבית». ثلاثة عناوين مختلفة تُظهر الصفحة نفسها بالضبط.'),
 ('page-guide','صفحة محتوى — دليل اختيار الإضاءة','/pages/guide-garden-lighting','doc','قسم Liquid واحد بحجم 37KB يطبع خمس صفحات مكتوبة جيداً بنفس القالب: شريط داكن معتم ← قائمة مرقّمة بخطوط ← زرّان. لا صور ولا مصابيح ولا حركة في صفحات عن الضوء عند الغسق. h1 مكرر.'),
 ('page-about','صفحة محتوى — من نحن','/pages/מי-אנחנו','doc','النص الذي يحمل موقف العلامة («כאשר מידע אינו מאומת…») مع صورة فانوس كيروسين من Pexels — ليس منتجاً تبيعه.'),
 ('page-shipping','صفحة محتوى — الشحن والإرجاع','/pages/shipping-delivery','doc','خارج قسم المحتوى المخصص: عنوان غير مرئي (كريمي على كريمي) والنص ملتصق بحافة الشاشة بلا هوامش.'),
 ('page-contact','اتصل بنا','/pages/contact-us','doc','نموذج Kalles بحقول بنية داكنة كلها إلزامية، يطلب «صورة للمكان» مع أن النموذج لا يقبل ملفات. كل روابط «שלחו תמונה» في المتجر تهبط هنا لأن رقم واتساب غير مضبوط.'),
 ('policy-shipping','السياسات (4 صفحات)','/policies/shipping-policy','doc','قالب Shopify المقفل بالمخطط القديم، عرض نص 1,410px، عنوان مكرر (h1 Shopify + h2 التاجر)، عناوين الإدارة بالإنجليزية («Refund policy»)، وسياسة الاتصال تحمل «Address: United Kingdom» وعبارات عربية مؤقتة.'),
 ('blog-news','المدونة','/blogs/news','off','منزلق يشير إلى مدونة تجريبية غير موجودة «fashion»: بطاقات ماكينة خياطة وعناوين «כותרת הפוסט שלך». المدونة الحقيقية «news» بلا مقالات.'),
]
chip={'on':('على النظام','ok'),'off':('Kalles افتراضي','bad'),'pdp':('PDP v2 — خارج النظام','warn'),'doc':('نص جيد، تصميم قالبي','warn')}
cards=[]
for k,title,url,st,desc in pages:
    c,cls=chip[st]
    cards.append(f'''<figure class="shot">
  <div class="shot__imgs"><img class="shot__d" src="{img(k,'desktop-fold')}" alt="الشاشة الأولى على سطح المكتب — {title}" loading="lazy"><img class="shot__m" src="{img(k,'mobile-fold')}" alt="الشاشة الأولى على الجوال — {title}" loading="lazy"></div>
  <figcaption><div class="shot__head"><h3>{title}</h3><span class="chip chip--{cls}">{c}</span></div><p class="shot__url" dir="ltr">{url}</p><p>{desc}</p></figcaption>
</figure>''')
html=f'''<title>الصفحات الجانبية — الجرد والخطة</title>
<meta name="description" content="جرد ثيم التطوير ElmsNest بلقطات حقيقية، ترتيب تصميم الصفحات الجانبية، وأسئلة المالك قبل البناء">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600&family=Frank+Ruhl+Libre:wght@700&family=Heebo:wght@400;500&display=swap">
<style>
:root{{--bg:#f2f4f8;--sur:#ffffff;--sur2:#e9edf3;--ink:#121a2b;--ink2:#4a5366;--mute:#6b7385;--gold:#8a5b0f;--glow:#a86d0c;--hair:rgba(18,26,43,.14);--ok:#1f7a45;--warn:#9a5a00;--bad:#a8323a;--chipbg:rgba(18,26,43,.06)}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0b1526;--sur:#111d33;--sur2:#172641;--ink:#f4eee3;--ink2:#c9c4b8;--mute:#8f95a3;--gold:#e9b96e;--glow:#ffd394;--hair:rgba(244,238,227,.14);--ok:#8fd3a5;--warn:#f0c674;--bad:#f28b82;--chipbg:rgba(244,238,227,.08)}}}}
:root[data-theme="dark"]{{--bg:#0b1526;--sur:#111d33;--sur2:#172641;--ink:#f4eee3;--ink2:#c9c4b8;--mute:#8f95a3;--gold:#e9b96e;--glow:#ffd394;--hair:rgba(244,238,227,.14);--ok:#8fd3a5;--warn:#f0c674;--bad:#f28b82;--chipbg:rgba(244,238,227,.08)}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:"IBM Plex Sans Arabic","Heebo",system-ui,-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.75;direction:rtl}}
.wrap{{width:min(1120px,100% - 40px);margin-inline:auto}}
h1,h2,h3{{font-family:"Amiri","Frank Ruhl Libre",serif;line-height:1.2;margin:0;text-wrap:balance;letter-spacing:0}}
h1{{font-size:clamp(34px,5vw,56px);font-weight:700}}
h2{{font-size:clamp(26px,3vw,36px);font-weight:700;margin-block:0 14px}}
h3{{font-size:21px;font-weight:700}}
p{{margin:0 0 12px;max-width:72ch}}
a{{color:var(--gold)}}
.eyebrow{{display:flex;align-items:center;gap:12px;font-size:13px;font-weight:500;letter-spacing:.04em;color:var(--gold);margin-bottom:12px}}
.eyebrow::before{{content:"";width:34px;height:1px;background:var(--gold)}}
header.top{{padding:64px 0 28px;border-bottom:1px solid var(--hair)}}
.lede{{font-size:19px;color:var(--ink2);max-width:60ch;margin-top:18px}}
.meta{{display:flex;flex-wrap:wrap;gap:10px 22px;color:var(--mute);font-size:14px;margin-top:22px}}
.meta b{{color:var(--ink);font-weight:500}}
nav.toc{{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--hair);padding:10px 0}}
nav.toc ul{{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:4px 18px;font-size:14px}}
nav.toc a{{color:var(--ink2);text-decoration:none;padding:6px 0;border-bottom:1px solid transparent}}
nav.toc a:hover,nav.toc a:focus-visible{{color:var(--gold);border-color:var(--gold)}}
section{{padding:56px 0 24px;scroll-margin-top:70px}}
section+section{{border-top:1px solid var(--hair)}}
.verdict{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0 32px;margin-top:24px}}
.verdict div{{padding:18px 0;border-top:1px solid var(--hair)}}
.verdict b{{display:block;font-family:"Amiri","Frank Ruhl Libre",serif;font-size:22px;margin-bottom:6px}}
.verdict p{{font-size:15px;color:var(--ink2)}}
.shots{{display:grid;gap:44px;margin-top:28px}}
.shot{{margin:0;display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:26px;align-items:start}}
.shot__imgs{{display:flex;gap:12px;align-items:flex-start}}
.shot__d{{width:74%;border:1px solid var(--hair);display:block}}
.shot__m{{width:24%;border:1px solid var(--hair);display:block}}
.shot__head{{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;margin-bottom:6px}}
.shot__url{{font-family:"IBM Plex Sans Arabic",monospace;font-size:12.5px;color:var(--mute);margin-bottom:8px;text-align:right}}
.shot figcaption p{{font-size:15px;color:var(--ink2)}}
.chip{{display:inline-block;font-size:12px;font-weight:500;padding:3px 10px;border-radius:999px;background:var(--chipbg);color:var(--ink2);white-space:nowrap}}
.chip--ok{{color:var(--ok)}}.chip--bad{{color:var(--bad)}}.chip--warn{{color:var(--warn)}}
.ledger{{list-style:none;margin:22px 0 0;padding:0}}
.ledger li{{display:grid;grid-template-columns:52px 1fr;gap:16px;padding:16px 0;border-top:1px solid var(--hair)}}
.ledger li:last-child{{border-bottom:1px solid var(--hair)}}
.ledger .n{{font-family:"Amiri","Frank Ruhl Libre",serif;font-size:30px;line-height:1;color:var(--glow);font-variant-numeric:tabular-nums}}
.ledger b{{font-weight:600}}
.ledger p{{font-size:15px;color:var(--ink2);margin:4px 0 0}}
table{{border-collapse:collapse;width:100%;font-size:15px;margin-top:20px}}
th,td{{text-align:right;vertical-align:top;padding:12px 10px;border-top:1px solid var(--hair)}}
th{{font-weight:600;color:var(--ink2);font-size:13.5px;letter-spacing:.02em}}
tr:last-child td{{border-bottom:1px solid var(--hair)}}
.tw{{overflow-x:auto}}
.steps{{counter-reset:s;list-style:none;padding:0;margin:20px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px 28px}}
.steps li{{counter-increment:s;padding-top:12px;border-top:1px solid var(--hair);font-size:15px;color:var(--ink2)}}
.steps li::before{{content:counter(s,decimal-leading-zero);display:block;font-family:"Amiri","Frank Ruhl Libre",serif;font-size:26px;color:var(--gold);margin-bottom:6px}}
.steps li b{{display:block;color:var(--ink);font-weight:600;margin-bottom:4px}}
.q{{list-style:none;padding:0;margin:20px 0 0}}
.q li{{display:grid;grid-template-columns:44px 1fr;gap:14px;padding:16px 0;border-top:1px solid var(--hair)}}
.q li:last-child{{border-bottom:1px solid var(--hair)}}
.q .n{{font-family:"Amiri","Frank Ruhl Libre",serif;font-size:24px;color:var(--glow);font-variant-numeric:tabular-nums;line-height:1.1}}
.q b{{font-weight:600}}
.q .why{{font-size:14.5px;color:var(--ink2);margin:4px 0 0}}
.q .rec{{font-size:14.5px;color:var(--ink);margin:6px 0 0;padding-inline-start:12px;border-inline-start:2px solid var(--gold)}}
.note{{border-inline-start:3px solid var(--gold);padding:8px 16px;background:var(--sur);margin:22px 0;font-size:15px}}
[lang="he"]{{font-family:"Heebo","IBM Plex Sans Arabic",sans-serif}}
h1 [lang="he"],h2 [lang="he"],h3 [lang="he"]{{font-family:"Frank Ruhl Libre","Amiri",serif}}
footer{{padding:40px 0 60px;color:var(--mute);font-size:13.5px;border-top:1px solid var(--hair);margin-top:40px}}
code{{font-family:ui-monospace,Menlo,monospace;font-size:.92em;direction:ltr;unicode-bidi:isolate;background:var(--chipbg);padding:1px 5px}}
@media (max-width:820px){{.shot{{grid-template-columns:1fr}}.shot__d{{width:70%}}.shot__m{{width:28%}}header.top{{padding-top:40px}}}}
@media (prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important}}}}
</style>
<header class="top"><div class="wrap">
<p class="eyebrow">ElmsNest · ثيم التطوير 154726400174 · 2 أيلول 2026</p>
<h1>الصفحات الجانبية: ما يعرضه الثيم اليوم، وترتيب العمل، والأسئلة</h1>
<p class="lede">جردت 31 صفحة حقيقية من ثيم التطوير (لقطات بتشغيل JavaScript الثيم، على 1440 و390)، وقرأت مصادر كل قالب وقسم. الخلاصة: الصفحة الرئيسية الجديدة هي الوحيدة على نظام التصميم؛ كل ما عداها قالب Kalles كريمي أو تصميم PDP سابق خارج النظام، وتحت رأس صفحة لا تُقرأ قائمته.</p>
<div class="meta"><span><b>31</b> صفحة مُجرودة</span><span><b>5</b> تدقيقات بصرية + دمج</span><span><b>121</b> ملف مصدر مُستخرج</span><span><b>20</b> سؤالاً للمالك</span><span>لم يُنشر شيء · لم يُبنَ شيء</span></div>
</div></header>
<nav class="toc"><div class="wrap"><ul><li><a href="#state">الحالة</a></li><li><a href="#shots">اللقطات</a></li><li><a href="#shared">ما هو مشترك ومعطّل</a></li><li><a href="#order">ترتيب العمل</a></li><li><a href="#pdp">صفحة المنتج تبيع أولاً</a></li><li><a href="#process">العملية</a></li><li><a href="#questions">الأسئلة</a></li></ul></div></nav>
<main>
<section id="state"><div class="wrap">
<p class="eyebrow">01 · الحالة</p><h2>سبع عائلات قوالب، واحدة فقط على النظام</h2>
<div class="verdict">
<div><b>الكولكشن</b><p>صفحة كتالوج Kalles كما تأتي من الصندوق: كريمية، Assistant، شريط بنّي، شريط أدوات بستة أيقونات، فلتر إنجليزي، وبطاقات ثلثا صورها ملصقات بنص عبري مطبوع.</p></div>
<div><b>صفحة المنتج</b><p>مرّت بجولة تصميم سابقة (PDP v2) بعشرة أقسام: نصوص بيع طويلة لكن قالبية وتتكرر حرفياً على كل منتج، صناديق، نصوص شمسية على مصابيح كهربائية، وبيانات فارغة على 26 من 27 منتجاً.</p></div>
<div><b>السلة والبحث و404</b><p>افتراضيات Kalles حرفياً: جدول بيج، شريط رمادي فارغ مكان سؤال البحث، عبرية متباعدة الأحرف على 404. درج السلة كريمي ويظهر فوق كل صفحة.</p></div>
<div><b>صفحات المحتوى</b><p>خمس صفحات مكتوبة جيداً داخل قسم Liquid واحد مُقفل بالكود، بلا صور ولا مصابيح، وبأداة واحدة تتكرر. صفحتا الشحن والاتصال خارجه وبعنوان غير مرئي.</p></div>
<div><b>السياسات والمدونة والحسابات</b><p>قالب Shopify المقفل بالمخطط القديم؛ مدونة بمحتوى تجريبي لماكينات خياطة؛ حسابات مستضافة عند Shopify وعناوين بالإنجليزية.</p></div>
<div><b>الفجوة</b><p>الصفحة الرئيسية وحدها تحمّل النواة المشتركة والخطوط والمصابيح. كل صفحة أخرى: <code>env2 base: False</code>، مخطط <code>scheme-1</code>، وقطع حاد من الكريمي إلى الأسود عند التذييل.</p></div>
</div>
</div></section>
<section id="shots"><div class="wrap">
<p class="eyebrow">02 · اللقطات الحقيقية</p><h2>الشاشة الأولى لكل قالب، سطح مكتب وجوال</h2>
<p>اللقطات من مرايا الصفحات الفعلية على ثيم التطوير، مُقدَّمة عبر خادم محلي حتى تعمل وحدات JavaScript الخاصة بـKalles (بدونها تختفي شبكات المنتجات كلها). اللقطات الكاملة للصفحات في <code>brief/inventory/&lt;page&gt;/http-*.png</code>.</p>
<div class="shots">{''.join(cards)}</div>
</div></section>
<section id="shared"><div class="wrap">
<p class="eyebrow">03 · قبل أي صفحة</p><h2>ما هو مشترك ومعطّل، ويجب أن يُصلح مرة واحدة</h2>
<ol class="ledger">
<li><span class="n">1</span><div><b>رأس الصفحة غير مقروء على كل الصفحات الجانبية.</b><p>الرأس شفاف بمخطط الليل (حبر فاتح) فوق أرضية كريمية: القائمة والبحث وزر الهامبرغر غير مرئية حتى يظهر الشريط الملتصق عند التمرير للأعلى. الحل على مستوى الموقع: أرضية داكنة أولى في كل قالب.</p></div></li>
<li><span class="n">2</span><div><b>النواة المشتركة مقيّدة بالصفحة الرئيسية.</b><p><code>elmsnest-v2-base</code> يُحمَّل من قسم الهيرو فقط وتدرّجه يستهدف <code>body.hdt-page-type-index</code>. يجب فصله إلى نواة عامة (الرموز، الخطوط، المصابيح، الأزرار، <code>window.env2</code>) تُحمَّل من <code>layout/theme.liquid</code> على كل قالب، وأرضية لكل قالب.</p></div></li>
<li><span class="n">3</span><div><b>شرائط Kalles الكريمية وعناوين h1 المكررة.</b><p>قسما <code>main-heading</code> و<code>top-list-collections</code> موجودان في قوالب الكولكشن والبحث والسلة والصفحات والحسابات، ويحملان الشريط البنّي وعنواناً مخفياً مكرراً. تُحذف من القوالب.</p></div></li>
<li><span class="n">4</span><div><b>درج السلة كريمي وزر «العودة للأعلى» بالألوان القديمة.</b><p>يُنقل درج السلة إلى مخطط <code>scheme-env2-night</code> مع تغيير الأرضية، ويُخفى زر العودة للأعلى في كل الصفحات كما في الرئيسية.</p></div></li>
<li><span class="n">5</span><div><b>خطوط واجهة Kalles ما زالت Assistant.</b><p>قائمة الرأس، الدرج، نافذة الإضافة السريعة والفلاتر تحتاج ضبط <code>--f_family_*</code> على Heebo وإلا ظهرت بخطين مختلفين.</p></div></li>
<li><span class="n">6</span><div><b>مخالفات الصدق التي ما زالت مرئية.</b><p>جدول المقارنة في صفحة المنتج ضد «منتج عام رخيص»، شارة «-25%» وسعر مشطوب على منتج واحد، خيارا فرز «الأكثر مبيعاً/شعبية»، عبارة «מחיר מבצע» المخفية على كل سعر عادي لقارئات الشاشة، ونحو 15 صورة رئيسية بادعاءات رقمية مطبوعة («50,000 שעות עבודה»). السجل الكامل في <code>brief/inventory/INVENTORY.md §3</code>.</p></div></li>
<li><span class="n">7</span><div><b>بطاقة منتج واحدة تخدم أربعة أماكن.</b><p><code>card-product1</code> يُستخدم في الكولكشن والبحث والمنتجات ذات الصلة وشوهد مؤخراً، ويستعمل الصورة رقم 0 دائماً. البطاقة الجديدة تحتاج قاعدة السعر (سعر واحد / نطاق / «מ־») وسجلّ فهارس الصور لكل منتج.</p></div></li>
</ol>
</div></section>
<section id="order"><div class="wrap">
<p class="eyebrow">04 · ترتيب العمل</p><h2>النواة أولاً، ثم صفحة المنتج، ثم ما يعيد استعمال ما تنتجه</h2>
<p>الترتيب مبني على شيئين: ما تعطيه كل جولة للجولة التالية، وتوجيهك أن صفحة المنتج هي الأهم وأنها يجب أن تبيع. لذلك تسبق صفحة المنتج الكولكشن؛ بطاقة «منتجات ذات صلة» التي تُصمَّم داخلها تصبح بطاقة الكتالوج.</p>
<div class="tw"><table>
<thead><tr><th>#</th><th>الجولة</th><th>لماذا هنا</th><th>ما تنتجه للجولات التالية</th></tr></thead>
<tbody>
<tr><td>0</td><td><b>النواة المشتركة</b> (هندسة + نقد واحد، بلا لوحة مفاهيم)</td><td>لا يمكن الحكم على أي رندر حقيقي قبل أن تصبح الأرضية والرأس والخطوط ودرج السلة على النظام.</td><td>فصل النواة، أرضية لكل قالب، حذف الشرائط الكريمية، مخطط الدرج، إخفاء العودة للأعلى، إصلاحات الصدق العامة، توسيع <code>lint.py</code>.</td></tr>
<tr><td>1</td><td><b>صفحة المنتج</b></td><td>أولويتك، ومكان البيع، وأصعب حزمة تقنية (الخيارات، شريط الشراء الملتصق، المعرض).</td><td>صندوق الشراء، سجلّ الخيارات بالسعر لكل طول/كمية، أداة «يناسب / لا يناسب» على مستوى المنتج، وبطاقة المنتجات ذات الصلة.</td></tr>
<tr><td>2</td><td><b>الكولكشن</b> (+ كل المنتجات؛ وقرار قائمة الكولكشنات)</td><td>مدخل المسار من «الأماكن الأربعة» في الرئيسية؛ يرث البطاقة من الجولة 1.</td><td>تكوين التصفح، قرار الفرز/الفلاتر، الحالة الفارغة، قاعدة الأرضية للصفحات الطويلة.</td></tr>
<tr><td>3</td><td><b>درج السلة + صفحة السلة</b></td><td>لحظة «المصباح يدخل السلة» بعد كل إضافة؛ تحتاج جلسة تفاعلية على الخادم المحلي.</td><td>الدرج أساسي والصفحة احتياط (سؤال 15)؛ شريط الشروط من سجلّ الرئيسية.</td></tr>
<tr><td>4</td><td><b>البحث (نتائج / لا نتائج / فارغ) + 404</b></td><td>صغيرتان، تعيدان استعمال البطاقة؛ لكل منهما أداة واحدة (مصباح لم يُضأ + الأماكن الأربعة).</td><td>—</td></tr>
<tr><td>5</td><td><b>صفحات المحتوى</b> (الدليل، لماذا شمسي، من نحن، الأسئلة، الشحن، المعالجة، الاتصال)</td><td>عائلة تحريرية واحدة بفكرة واحدة وتنويع لكل صفحة؛ صفحة الاتصال تنتظر رقم واتساب.</td><td>استبدال القسم المقفل بالكود بقوالب JSON لكل صفحة.</td></tr>
<tr><td>6</td><td><b>السياسات، كلمة المرور، الحسابات</b></td><td>السياسات ترميز مقفل (طباعة وخطوط شعرية من <code>theme.liquid</code>)؛ كلمة المرور مهمة ما دامت الخطة «Pause and Build»؛ الحسابات فقط إن كانت قوالبنا (سؤال 9).</td><td>—</td></tr>
</tbody></table></div>
<p class="note">الجولتان 0 و1 تتداخلان: لوحة مفاهيم صفحة المنتج (نماذج HTML غير متصلة) تبدأ فوراً بينما تُهندَس النواة.</p>
</div></section>
<section id="pdp"><div class="wrap">
<p class="eyebrow">05 · توجيهك</p><h2>صفحة المنتج تُحكَم أولاً كصفحة بيع</h2>
<p>قبل لوحة المفاهيم يُكتب «عمود الإقناع»: أسئلة المشتري بترتيب ظهورها في رأسه، ولكل سؤال أداة ملموسة على الصفحة تجيبه وتدفعه خطوة. كل مفهوم من الخمسة يجب أن ينفّذ العمود كاملاً، ولجنة التحكيم تضم حكم تحويل بوزن 40% من الدرجة، وسترى المفاهيم الخمسة وحكم اللجنة قبل أي بناء.</p>
<div class="tw"><table>
<thead><tr><th>#</th><th>سؤال المشتري</th><th>الأداة على الصفحة</th><th>المصدر الصادق</th></tr></thead>
<tbody>
<tr><td>1</td><td>ما هذا، وهل هو لمكاني؟</td><td>الشاشة الأولى: المصباح مضاءً في مكانه ليلاً، كلمة المكان (<span lang="he">שביל / קיר / גינה / מרפסת</span>) مع عبارة «<span lang="he">מתאים כדי</span>» المعتمدة، السعر، الشراء.</td><td>الكولكشن، الأزواج الأربعة المعتمدة</td></tr>
<tr><td>2</td><td>هل سيعمل حيث أريد وضعه؟</td><td>أداة «يناسب / لا يناسب» على مستوى المنتج (الفاصل القابل للسحب من الرئيسية أو منتقي مكان) — السلبية الواحدة من الأربع المعتمدة فقط.</td><td>BRIEF §3، حقل <code>not_fit_for</code> عند تعبئته</td></tr>
<tr><td>3</td><td>كيف يبدو ليلاً فعلاً؟</td><td>معرض ليلي يُضاء عند الوصول، مع إشارة مقياس (الارتفاع بالسنتيمتر، المسافة بين الوحدات).</td><td>الصور 1 فما فوق، نقاط المواصفات</td></tr>
<tr><td>4</td><td>ماذا أستلم بالضبط، وكم يكلف الطويل؟</td><td>سجلّ الخيارات: كل طول/كمية بسعره وسعر الوحدة؛ الأطقم (2/4/6) كتغطية («ممر 6 أمتار = 4 وحدات»).</td><td><code>product.variants</code>، سعر الوحدة</td></tr>
<tr><td>5</td><td>ما الذي قد يخذلني؟</td><td>الحقائق التي تخفض المخاطر بصراحة: مصدر الطاقة، درجة IP، ساعات العمل بعد شحن كامل، ملاحظة الشتاء للشمسي؛ ما لا نعرفه لا نزعمه.</td><td>نقاط الوصف، الحقول المخصصة (سؤال 17)</td></tr>
<tr><td>6</td><td>ماذا يحدث بعد الطلب؟</td><td>الأرقام الأربعة (0 ₪ نقطة استلام / 29.90 للباب · 8–17 يوماً · إلغاء 14 يوماً · فحص الصورة) — سجلّ الرئيسية مضغوطاً.</td><td>السياسات، صياغة الشروط المرخّصة</td></tr>
<tr><td>7</td><td>لماذا من هنا وليس من سوق إلكتروني؟</td><td>ليس جدول مقارنة: وعد المتخصص كأداة — «نقول لك متى لا»، مواصفات بالعبرية، إنسان تسأله قبل الطلب (واتساب حين يُضبط الرقم).</td><td>«<span lang="he">מי אנחנו</span>»</td></tr>
<tr><td>8</td><td>هل أستطيع خطوة أصغر من الشراء؟</td><td>خطوة الالتزام المنخفض: إرسال صورة المكان؛ أو إضافة وحدة واحدة وتقرير الطقم لاحقاً.</td><td>واتساب / الاتصال</td></tr>
</tbody></table></div>
<p class="note">داخل قواعد الصدق: لا دليل مُختلق (تقييمات، أعداد، استعجال)، لا ادعاءات مقارنة عن الآخرين، لا نصوص شمسية على منتجات كهربائية (فرع مصدر الطاقة في Liquid)، لا حقائق مكتوبة يدوياً (الأرقام من الخيارات والحقول والوصف فقط).</p>
</div></section>
<section id="process"><div class="wrap">
<p class="eyebrow">06 · العملية لكل صفحة</p><h2>نفس عملية الصفحة الرئيسية، بإضافتين لصفحة المنتج</h2>
<ol class="steps">
<li><b>الموجز</b>حقائق القالب، البيانات الموجودة، نظام التصميم، القيود الصلبة، المستوى المطلوب، قائمة الممنوعات، وسجلّ الصور. لصفحة المنتج: عمود الإقناع أولاً.</li>
<li><b>خمسة مفاهيم متباعدة</b>خمسة مصممين ببذور مختلفة جذرياً، كل منهم ينتج نموذج HTML كاملاً بمنتجات وأسعار وصور وخطوط حقيقية، ويصوّره وينقد نفسه من اللقطات.</li>
<li><b>التحكيم من اللقطات</b>مدير إبداعي · متسوق إسرائيلي من الجوال · علامة + جدوى Liquid. لصفحة المنتج: + حكم تحويل (40%) ورئيس نصوص عبرية. ثم قائد يركّب المواصفة.</li>
<li><b>نقطة توقف عندك (صفحة المنتج فقط)</b>لقطات المفاهيم الخمسة وحكم اللجنة قبل البناء.</li>
<li><b>البناء</b>النواة أولاً، مهندس لكل قسم، معاينة غير متصلة + <code>lint.py</code>، مُدمِج يوفّق المخططات مع القالب، نشر على ثيم التطوير، مرآة ولقطات بتشغيل JS.</li>
<li><b>النقد العدائي</b>مدير إبداعي · متسوق عبري ينفّذ مسار الشراء فعلاً (خيار → سعر → إضافة → درج) · مصمم طباعة عبري · QA يختبر اللمس ولوحة المفاتيح وتقليل الحركة وبدون JS. فرز → حزم إصلاح → إعادة نشر → تحقق.</li>
<li><b>حكمك</b>القائد ينظر بنفسه إلى الرندر الحقيقي، ثم أنت الحكم الأخير. لا يُنشر شيء بدون كلمة «انشر» منك.</li>
</ol>
</div></section>
<section id="questions"><div class="wrap">
<p class="eyebrow">07 · الأسئلة</p><h2>ما يوقف الجولتين 0 و1، وما يمكن حسمه بلا تصميم</h2>
<p>القائمة الكاملة (20 سؤالاً) في <code>brief/inventory/INVENTORY.md §5</code>. هنا ما يغيّر العمل فعلاً، مع توصيتي حيث توجد.</p>
<h3 style="margin-top:26px">يوقف البناء</h3>
<ol class="q">
<li><span class="n">1</span><div><b>ما رقم واتساب المتجر؟</b><p class="why">الإعداد فارغ، فكل روابط «שלחו תמונה» في كل الصفحات تهبط على نموذج اتصال لا يقبل صوراً، وصفحة المنتج تعد «בוואטסאפ».</p></div></li>
<li><span class="n">2</span><div><b>هل تصميم PDP v2 الحالي أساس نعيد تلبيسه، أم نستبدله كلياً؟</b><p class="why">هو نصف الكود المخصص في الثيم، ولا شيء منه على النظام.</p><p class="rec">توصيتي: نستبدل التكوين واللوحة، ونحتفظ بأصول النصوص (وصف <code>.elms-sales</code> على 27 منتجاً وصياغة الشروط).</p></div></li>
<li><span class="n">3</span><div><b>الصور الرئيسية بنص مطبوع (نحو 15 منتجاً): تُستبدل بصور نظيفة أم نقفل الفهارس 1–3 نهائياً؟</b><p class="why">كل بطاقة ومعرض وقائمة ذات صلة تعتمد على هذا القرار؛ إحدى الصور تحمل علامة «LUMIÈRE» لطرف ثالث.</p></div></li>
<li><span class="n">4</span><div><b>هل ستُملأ حقول المواصفات و«لا يناسب» والأسئلة لباقي 26 منتجاً؟</b><p class="why">تقرر إن كانت لوحة المواصفات وأداة «يناسب/لا يناسب» تُبنى من البيانات أو تُرسم يدوياً.</p><p class="rec">توصيتي: نستخرجها بسكربت من نقاط الوصف الموجودة إلى جدول تراجعه وتعتمده، ثم نكتبها في الحقول.</p></div></li>
<li><span class="n">5</span><div><b>هل يوجد «مبيعات» أصلاً؟</b><p class="why">كولكشن <span lang="he">מבצעים</span> غير منشور (يعطي 404) لكنه في القوائم، ومنتج واحد يحمل سعراً مشطوباً 199.90 ← 149.90. العلامة تمنع أدوات الاستعجال؛ الشطب مسموح فقط إن كان 199.90 سعراً حقيقياً بيع به.</p></div></li>
<li><span class="n">6</span><div><b>هل الفلاتر والفرز مهمة لـ27 منتجاً؟</b><p class="why">الفلاتر الموجودة: التوفر والسعر فقط، ولا بيانات لواط/IP/منطقة. خيارا «الأكثر مبيعاً/شعبية» يوحيان بأرقام لا تملكها.</p><p class="rec">توصيتي: لا شريط أدوات؛ روابط الأماكن + ترتيب السعر.</p></div></li>
<li><span class="n">7</span><div><b>أي مجموعة أسماء للكولكشنات هي المعتمدة؟</b><p class="why">القائمة تقول «תאורת שביל, עמוד וגינה»، التذييل «גרילנדות ודקורטיבי»، الدليل «הארה ממוקדת»، وقوائم v4 «שביל ומדרגות / כניסה וקיר…». كل عنوان صغير وفتات خبز وبطاقة يعتمد عليها. وهل التصنيف نهائي رغم أن «تاورات كير الشمسية» تضم ثلاثة مصابيح كهربائية وأحدها للداخل؟</p></div></li>
<li><span class="n">8</span><div><b>بعد الإضافة للسلة: الدرج أم صفحة السلة هي التجربة الأساسية؟</b><p class="rec">توصيتي: الدرج، والصفحة احتياط بلا JS.</p></div></li>
<li><span class="n">9</span><div><b>حكم الصفحة الرئيسية، صورة الهيرو ≥2000px، وشعار مركّب (أيقونة + ElmsNest).</b><p class="why">كل صفحة جانبية ترث الأرضية والخط وقرار الرأس من نظام الرئيسية؛ 404 والسياسات والسلة لا تملك صورة تحمل الهوية.</p></div></li>
</ol>
<h3 style="margin-top:34px">يُحسم بلا تصميم (أوصي بنعم)</h3>
<ol class="q">
<li><span class="n">10</span><div><b>سحب المدونة من الواجهة</b> (<code>news</code> بلا مقالات، ومنزلق يعرض محتوى تجريبياً).</div></li>
<li><span class="n">11</span><div><b>إبقاء الحسابات مستضافة عند Shopify</b> فلا تُصمَّم قوالب <code>customers/*</code> السبعة.</div></li>
<li><span class="n">12</span><div><b>نشر «הצהרת נגישות»</b> (موجودة غير منشورة منذ 1 أيلول) — رابط في التذييل إلى 404 مسؤولية قانونية لا خيار تخطيط.</div></li>
<li><span class="n">13</span><div><b>عناوين السياسات بالعبرية في الإدارة</b> («Refund policy» اليوم) وحسم «מדיניות» أم «תקנון»، وتصحيح سياسة الاتصال (عنوان حقيقي وهاتف وח.פ. بدل «United Kingdom» والعبارات العربية المؤقتة).</div></li>
<li><span class="n">14</span><div><b>حذف قوالب Kalles التجريبية</b> (men/women/kids، store-locator بمفتاح Mapbox حي، faq-2، compare…) — تحمل عدّادات و«Best Sellers» على بعد نقرة من المحرر.</div></li>
<li><span class="n">15</span><div><b>أي قائمة تُعتمد</b>: <code>main-menu</code> كما هي، أم تعديل التسليم (קולקציות ← <code>/#env2-places</code> وحذف שאלות נפוצות)، أم مجموعة v4.</div></li>
</ol>
</div></section>
</main>
<footer><div class="wrap">
<p>المصادر في الفرع <code>claude/design-sidebar-pages-3991tn</code>: <code>brief/side-pages/PLAN.md</code> (خطة التسجيل) · <code>brief/inventory/INVENTORY.md</code> (الجرد المدمج + 20 سؤالاً) · <code>brief/inventory/AUDIT-*.md</code> (تدقيق كل عائلة) · <code>brief/inventory/THEME-SRC.md</code> (مصادر القوالب) · <code>brief/side-pages/OWNER-NOTES.md</code> (توجيهاتك حرفياً). ثيم التطوير غير منشور؛ المتجر الحي لم يُمس.</p>
</div></footer>
'''
open(OUT,'w',encoding='utf-8').write(html)
print('written',os.path.getsize(OUT)//1024,'KB')
