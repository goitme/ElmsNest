# -*- coding: utf-8 -*-
import base64,os
IMG='/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/report2-img'
OUT='/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/pdp-ruling.html'
def img(n): return 'data:image/jpeg;base64,'+base64.b64encode(open(f'{IMG}/{n}.jpg','rb').read()).decode()

concepts=[
 ('switch','המتغ','8.64','1',
  'كل اختيار مِفتاح يغيّر ضوء المنتج أمام عينيك: الطول يُشعل نوراً إضافياً على سلسلة حقيقية والسعر يتحرك معه، الكمية ترسم عموداً آخر على الممر، والواط ودرجة اللون يغيّران الهالة على الحائط. وحين تُحوّل المفتاح إلى ما لا تصلح له المنورة، لا تُضيء.',
  'الشاشة الأولى على الهاتف تحتوي كل شيء بلا تمرير: صورة ليلية للمنتج، المكان والعبارة المعتمدة، الاسم، 89.90 ₪، «إضافة للسلة»، الأرقام الأربعة في سطر، والأطوال الستة بأسعارها.'),
 ('dialogue','الشيحة','8.41','2',
  'الصفحة محضر محادثة مع المتخصص: ثماني نقلات، كل منها تردّد المشتري نفسه بخط Frank Ruhl Libre كبير بين علامتَي اقتباس، يُجاب عليه بصوت العلامة ويُثبته جهاز يُضيء — وأحدها مصباح يرفض أن يُضيء.',
  'أفضل كتابة بين الخمسة. حكم النصوص العبرية رتّبه أولاً. أُخذ منه سطر المعنى لكل طول وصيغة العناوين كسؤال المشتري.'),
 ('place','المكان','8.51','3',
  'الصفحة تفتح على مكان المشتري نفسه ليلاً — مرفسة، ممر، مدخل — والمنتج هو الشيء الوحيد الذي يضيئه؛ وكل شاشة بعدها سؤال من أسئلة المكان: كم شمساً يأخذ؟ كم متراً يلزم للدوران؟ كم وحدة على الممر؟',
  'حكم العلامة رتّبه أولاً لأنه الأقرب لموقف المتجر. أُخذ منه سؤال «كم شمساً يأخذ المكان؟» كأداة تحلّ محل التحذير.'),
 ('ledger','الپنكس','8.34','4',
  'مصفوفة الخيارات هي البطل: كل طول صفّ على خط شعري — رقم أمتار ضخم، عدد النورات، سعر المتر، والسعر بالتوهّج — فتُقرأ 24 خياراً كجدول واحد تقرره في عشر ثوانٍ، والصفّ الذي تختاره هو الشيء الوحيد الذي يُضيء.',
  'أوضح أداة قرار. أُخذ منه سعر المتر، وسطر الشروط تحت الزر، ورابط «لمن لا يناسب» بجانب الزر، وجملة الوحدات.'),
 ('walk','ليلة المشي','7.25','5',
  'الصفحة مشيٌ نحو المنورة: المنتج نفسه مصوَّراً من بعيد، ومن وسط الحديقة، ومن مسافة يد — ثلاث لحظات ليلية ملء الشاشة، والكلمات مجرد تعليقات، وصندوق الشراء بطاقة تسافر معك.',
  'أجمل جوّ وأضعف بيع: الشاشة الأولى لا تحمل زر شراء بل «لبحيرت أورخ وتسبع»، والسعر «من 89.90» فقط. أُخذ منه تكوين صفحة مصباح الحائط.'),
]
graf=[
 ('dialogue','سطر معنى لكل طول في الجدول','«20 نورة · لزاوية جلوس صغيرة أو طاولة واحدة» … «200 نورة · تزيين فضاء كامل». هذا وحده ما يحسم بين 9.5 و11 متراً، وكله مقتبس من وصف المنتج.'),
 ('place','سؤال الشمس كأداة','«كم شمساً يأخذ المكان في النهار؟» يوضع تحت المفتاح مباشرة، فيصير قيد الطاقة الشمسية جواب المشتري لا تحذيراً منّا.'),
 ('ledger','سعر المتر وسطر الشروط تحت الزر','و«لمن هذا لا يناسب ←» بجانب زر الشراء: عرض السلبية في لحظة الالتزام هو موقف المتجر كله في ثلاث كلمات.'),
 ('ledger','عناوين الأرقام الأربعة','«أربعة أرقام، قبل أن تدفع.» + «ليست حروفاً صغيرة. حروف كبيرة، في مكان ظاهر، بجانب الزر.» تبيع الشروط كميزة بدل دفنها.'),
 ('place','جملة وحدة المنتجات ذات الصلة','«بلا نجوم وبلا (الأكثر مبيعاً) — ليس عندنا بعد ما نقيسه.» أفضل جملة كُتبت في هذه الجولة: تحوّل الغياب إلى دليل على الموقف.'),
 ('walk','تكوين صفحة مصباح الحائط','لقطة قريبة للمنتج بجانب واجهة مضاءة والعنوان يركب الحدّ بينهما — يعالج أضعف الأبطال الثلاثة.'),
]
flow=[('fit','الشاشة الثانية: المفتاح','«يوجد مفتاح واحد لا تعرفه»: مفتاح حقيقي بين «مناسب كي تصنع جوّاً» و«يحتاج ضوءاً قوياً — ليست هذه غايتها». السلسلة تحته تنطفئ فعلاً.'),
 ('ledger','الجدول','ستة أطوال، كل صفّ بسعره وسعر متره وزر إضافة خاص به. اللون اختيار منفصل لا يغيّر السعر، ومكتوب ذلك صراحة.'),
 ('facts','الحقائق','«ما هو مكتوب هنا — صحيح. ما هو غير معروف — غير مكتوب.» IP65 بحجم جدار، وبقية الحقائق من نقاط الوصف فقط.'),
 ('ask','الخطوة الصغيرة','«ما زلت غير واثق؟ لا داعي أن تكون.» اقتباس «من نحن» ثم إرسال صورة المكان — وزر الشراء يبقى في متناول اليد.'),
]
cards=''.join(f'''<article class="c" id="c-{k}">
 <header class="c__h"><span class="rank">{r}</span><div><h3>{ar} <span class="lat" dir="ltr">{k}</span></h3><p class="score"><span>{sc}</span> / 10</p></div></header>
 <img src="{img(k)}" alt="الشاشة الأولى لمفهوم {ar} على سطح المكتب والجوال" loading="lazy">
 <p class="idea">{idea}</p><p class="note">{note}</p>
</article>''' for k,ar,sc,r,idea,note in concepts)
grafts=''.join(f'<li><span class="from" dir="ltr">{f}</span><div><b>{d}</b><p>{w}</p></div></li>' for f,d,w in graf)
flows=''.join(f'<figure class="fl"><img src="{img("win-"+n)}" alt="{t}" loading="lazy"><figcaption><b>{t}</b>{d}</figcaption></figure>' for n,t,d in flow)

html=f'''<title>حكم صفحة المنتج</title>
<meta name="description" content="خمسة مفاهيم لصفحة منتج ElmsNest، حكم خمسة محكّمين، الفائز والمواصفة الجاهزة للبناء">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=IBM+Plex+Sans+Arabic:wght@300;400;500;600&family=Frank+Ruhl+Libre:wght@700&display=swap">
<style>
:root{{
 --bg:#070b13;--bg2:#0d1524;--ink:#f4eee3;--ink2:#c9c4b8;--mute:#8f95a3;
 --gold:#e9b96e;--glow:#ffd394;--hair:rgba(244,238,227,.13);--scrim:rgba(6,9,16,.6);
 --serif:"Amiri","Frank Ruhl Libre",serif;--sans:"IBM Plex Sans Arabic",system-ui,-apple-system,"Segoe UI",sans-serif;
}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-weight:300;font-size:16px;line-height:1.75;direction:rtl;-webkit-font-smoothing:antialiased}}
.wrap{{width:min(1180px,100% - 44px);margin-inline:auto}}
h1,h2,h3{{font-family:var(--serif);font-weight:700;line-height:1.15;margin:0;text-wrap:balance}}
h1{{font-size:clamp(38px,6vw,72px)}}
h2{{font-size:clamp(28px,3.4vw,42px);margin-bottom:14px}}
h3{{font-size:23px}}
p{{margin:0 0 14px;max-width:74ch}}
a{{color:var(--gold)}}
.eyebrow{{display:flex;align-items:center;gap:13px;font-size:12px;font-weight:500;letter-spacing:.14em;color:var(--gold);margin-bottom:14px}}
.eyebrow::before{{content:"";width:36px;height:1px;background:var(--gold);flex:none}}
.lat{{font-family:var(--sans);font-size:.62em;font-weight:400;color:var(--mute);letter-spacing:.04em;unicode-bidi:isolate}}
header.top{{padding:70px 0 44px;position:relative;overflow:hidden}}
header.top::after{{content:"";position:absolute;inset-inline-start:-10%;top:-40%;width:70%;height:150%;background:radial-gradient(closest-side,rgba(255,211,148,.10),transparent 70%);pointer-events:none}}
.lede{{font-size:20px;color:var(--ink2);max-width:56ch;margin-top:20px;position:relative}}
.verdict{{margin-top:34px;padding:26px 30px;background:var(--bg2);border-inline-start:2px solid var(--glow);position:relative}}
.verdict b{{color:var(--glow);font-weight:500}}
.verdict p:last-child{{margin-bottom:0}}
nav.toc{{position:sticky;top:0;z-index:9;background:rgba(7,11,19,.94);backdrop-filter:blur(10px);border-block:1px solid var(--hair);padding:11px 0}}
nav.toc ul{{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:2px 22px;font-size:14px}}
nav.toc a{{color:var(--ink2);text-decoration:none;padding:5px 0;border-bottom:1px solid transparent}}
nav.toc a:hover,nav.toc a:focus-visible{{color:var(--glow);border-color:var(--glow)}}
section{{padding:62px 0 30px;scroll-margin-top:64px}}
section+section{{border-top:1px solid var(--hair)}}
.concepts{{display:grid;gap:54px;margin-top:30px}}
.c__h{{display:flex;align-items:flex-start;gap:18px;margin-bottom:16px}}
.rank{{font-family:var(--serif);font-size:52px;line-height:.9;color:transparent;-webkit-text-stroke:1px rgba(244,238,227,.45);flex:none;font-variant-numeric:tabular-nums}}
#c-switch .rank{{color:var(--glow);-webkit-text-stroke-color:transparent;text-shadow:0 0 34px rgba(255,211,148,.45)}}
.score{{margin:2px 0 0;font-family:var(--serif);font-size:19px;color:var(--mute);font-variant-numeric:tabular-nums}}
.score span{{color:var(--glow);font-size:26px}}
.c img{{width:100%;display:block;border:1px solid var(--hair)}}
.idea{{margin-top:16px;font-size:17px;color:var(--ink)}}
.note{{color:var(--ink2);font-size:15px}}
#c-switch{{padding:22px;background:linear-gradient(180deg,rgba(255,211,148,.05),transparent 60%);outline:1px solid rgba(233,185,110,.28)}}
.flows{{display:grid;gap:40px;margin-top:26px}}
.fl{{margin:0;display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:26px;align-items:start}}
.fl img{{width:100%;display:block;border:1px solid var(--hair)}}
.fl figcaption{{font-size:15px;color:var(--ink2)}}
.fl b{{display:block;font-family:var(--serif);font-size:22px;color:var(--ink);margin-bottom:8px;font-weight:700}}
ol.g{{list-style:none;padding:0;margin:24px 0 0}}
ol.g li{{display:grid;grid-template-columns:96px 1fr;gap:20px;padding:18px 0;border-top:1px solid var(--hair)}}
ol.g li:last-child{{border-bottom:1px solid var(--hair)}}
.from{{font-size:12.5px;letter-spacing:.06em;color:var(--gold);padding-top:5px;unicode-bidi:isolate}}
ol.g b{{font-weight:600;color:var(--ink)}}
ol.g p{{margin:5px 0 0;font-size:15px;color:var(--ink2)}}
.changes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:0 34px;margin-top:22px}}
.changes div{{padding:20px 0;border-top:1px solid var(--hair)}}
.changes b{{display:block;font-family:var(--serif);font-size:21px;margin-bottom:7px;color:var(--glow);font-weight:700}}
.changes p{{font-size:15px;color:var(--ink2);margin:0}}
.risk{{margin-top:24px;padding:24px 28px;background:var(--bg2);border-inline-start:2px solid var(--gold)}}
.risk p:last-child{{margin-bottom:0}}
ol.next{{counter-reset:n;list-style:none;padding:0;margin:22px 0 0}}
ol.next li{{counter-increment:n;display:grid;grid-template-columns:44px 1fr;gap:16px;padding:16px 0;border-top:1px solid var(--hair)}}
ol.next li:last-child{{border-bottom:1px solid var(--hair)}}
ol.next li::before{{content:counter(n,decimal-leading-zero);font-family:var(--serif);font-size:24px;color:var(--gold);font-variant-numeric:tabular-nums}}
ol.next b{{font-weight:600}}
ol.next p{{margin:4px 0 0;font-size:15px;color:var(--ink2)}}
.he{{font-family:"Frank Ruhl Libre",var(--serif);unicode-bidi:isolate}}
code{{font-family:ui-monospace,Menlo,monospace;font-size:.86em;direction:ltr;unicode-bidi:isolate;background:rgba(244,238,227,.07);padding:1px 6px;color:var(--ink2)}}
footer{{padding:40px 0 64px;color:var(--mute);font-size:13.5px;border-top:1px solid var(--hair);margin-top:34px}}
@media (max-width:820px){{.fl{{grid-template-columns:1fr}}ol.g li{{grid-template-columns:1fr;gap:6px}}.from{{padding-top:0}}}}
@media (prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important}}}}
</style>
<header class="top"><div class="wrap">
<p class="eyebrow">ElmsNest · صفحة المنتج · الجولة الأولى · 2 أيلول 2026</p>
<h1>خمسة مفاهيم، خمسة محكّمين،<br>وصفحة واحدة تبيع.</h1>
<p class="lede">بنى خمسة مصممين خمس صفحات منتج كاملة ببذور متباعدة، ثلاثة نماذج لكل واحد (غرلندة بـ24 خياراً، مصباح ممر، مصباح حائط كهربائي). حكمها خمسة محكّمين من اللقطات، ومعيار «هل تبيع؟» وحده يحمل 40% من الدرجة.</p>
<div class="verdict"><p><b>الفائز: «المتغ» — الصفحة كخشبة يشغّلها الزبون.</b> كل اختيار يغيّر ضوء المنتج أمام العينين، وحين تُحوّل المفتاح إلى ما لا تصلح له المنورة، لا تُضيء.</p>
<p>فاز لأنه الوحيد الذي وضع كل شيء في الشاشة الأولى على الهاتف بلا تمرير: صورة ليلية، المكان والعبارة المعتمدة، الاسم، السعر، زر الشراء، الأرقام الأربعة، والأطوال الستة بأسعارها. عند اثنين لا يوجد زر شراء في الشاشة الأولى أصلاً، وعند ثالث الشاشة الأولى جدول بلا صورة.</p></div>
</div></header>
<nav class="toc"><div class="wrap"><ul><li><a href="#five">المفاهيم الخمسة</a></li><li><a href="#flow">كيف تسير الصفحة</a></li><li><a href="#grafts">ما أُخذ من الباقين</a></li><li><a href="#diff">ما سيتغيّر</a></li><li><a href="#risk">الخطر</a></li><li><a href="#next">التالي</a></li></ul></div></nav>
<main>
<section id="five"><div class="wrap"><p class="eyebrow">01 · المفاهيم</p><h2>الخمسة، بترتيب الدرجة المرجّحة</h2>
<p>الدرجة تجمع خمسة محكّمين: مدير إبداعي، خبيرة تحويل إسرائيلية تشتري من الهاتف (وزنها مضاعف)، رئيس نصوص عبرية، حارس العلامة، ومهندس Shopify. الصورة اليسرى سطح مكتب، واليمنى هاتف — كلتاهما الشاشة الأولى فقط.</p>
<div class="concepts">{cards}</div></div></section>
<section id="flow"><div class="wrap"><p class="eyebrow">02 · الفائز</p><h2>كيف تسير الصفحة بعد الشاشة الأولى</h2>
<p>كل شاشة مؤلَّفة بشكل مختلف، ولا يوجد صندوق واحد مكرر. هذه أربع محطات من الصفحة الكاملة (7,882 بكسل على سطح المكتب).</p>
<div class="flows">{flows}</div></div></section>
<section id="grafts"><div class="wrap"><p class="eyebrow">03 · الطعوم</p><h2>ما أُخذ من المفاهيم الخاسرة</h2>
<p>الفائز لا يُبنى كما هو: ستة أجهزة من المفاهيم الأخرى تدخل المواصفة، لأن كلاً منها يحلّ شيئاً لم يحله الفائز.</p>
<ol class="g">{grafts}</ol></div></section>
<section id="diff"><div class="wrap"><p class="eyebrow">04 · فروق</p><h2>ثلاثة أشياء ستبدو مختلفة عن النموذج</h2>
<div class="changes">
<div><b>ألوان الضوء الأربعة</b><p>لن تظهر كأربع دوائر في صفّ — هذا ممنوع بقواعدنا. ستكون اختياراً واحداً هادئاً داخل سطر الشراء.</p></div>
<div><b>النقاط على الخلفية</b><p>النقاط المنثورة اليوم على صورة الخلفية تختفي: تبدو كشبكة فوق الصورة. النورات تبقى على الخيط وحده.</p></div>
<div><b>صفحة مصباح الحائط</b><p>لن يُكتب «توصيل كهربائي»: بيانات المنتج لا تذكر مصدر الطاقة، ونحن لا نكتب ما لا نعرفه.</p></div>
</div></div></section>
<section id="risk"><div class="wrap"><p class="eyebrow">05 · الخطر</p><h2>خطر واحد يستحق أن تعرفه</h2>
<div class="risk"><p>سنبني آلية الشراء من جديد (اختيار الطول، السعر، الإضافة للسلة، الشريط السفلي) بدل الاتكاء على آلية قالب Kalles. هذا ما يسمح لجدول الأسعار أن يكون الصفحة نفسها، وهو أيضاً ما يجعل الصفحة تعمل بلا JavaScript.</p>
<p>النقطة التي يجب التأكد منها عملياً: أن درج السلة يُفتح بعد «إضافة للسلة». إن لم يُفتح، نسقط إلى صفحة السلة بلا كسر.</p></div></div></section>
<section id="next"><div class="wrap"><p class="eyebrow">06 · التالي</p><h2>ما سيحدث بعد كلمتك</h2>
<ol class="next">
<li><div><b>حكمك على المفهوم الفائز</b><p>موافقة، أو تبديل بمفهوم آخر، أو تعديل. المواصفة الجاهزة للبناء مكتوبة (921 سطراً) وتنتظر كلمتك فقط.</p></div></li>
<li><div><b>بناء صفحة المنتج على ثيم التطوير</b><p>ثمانية أقسام جديدة، ثم نقد عدائي ينفّذ مسار الشراء فعلاً، ثم تعرضها أنت. لا نشر على المتجر الحي.</p></div></li>
<li><div><b>جدول المواصفات ينتظر موافقتك</b><p>27 منتجاً، كل قيمة مقتبسة من وصف المنتج نفسه في <code>METAFIELD-SHEET.md</code>. كتابتها تغيّر صفحات المنتجات الحية، فلن تُكتب قبل موافقتك. أربعة بنود تحتاج قرارك: مصدر الطاقة لثلاثة منتجات، وواط الپروجكتور، وأربع قيم «لا يناسب»، وهل «للاستعمال الداخلي» يصير زوجاً معتمداً خامساً.</p></div></li>
<li><div><b>ثم الكولكشن</b><p>بطاقة المنتج التي تُصمَّم داخل صفحة المنتج تصبح بطاقة الكتالوج، فتبدأ الجولة الثانية وقد نصف عملها جاهز.</p></div></li>
</ol></div></section>
</main>
<footer><div class="wrap"><p>المصادر في الفرع <code>claude/design-sidebar-pages-3991tn</code>: المواصفة <code>brief/side-pages/pdp/WINNING-SPEC.md</code> · الحكم بالعبرية <code>RULING.md</code> · الموجز <code>BRIEF.md</code> · النماذج <code>concepts/&lt;key&gt;/</code> · جدول المواصفات <code>METAFIELD-SHEET.md</code>. ثيم التطوير 154726400174 غير منشور، والمتجر الحي لم يُمس.</p></div></footer>
'''
open(OUT,'w',encoding='utf-8').write(html)
print('written',os.path.getsize(OUT)//1024,'KB')
