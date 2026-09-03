# -*- coding: utf-8 -*-
import base64,os
IMG='/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/report3-img'
OUT='/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/pdp-built.html'
def img(n): return 'data:image/jpeg;base64,'+base64.b64encode(open(f'{IMG}/{n}.jpg','rb').read()).decode()
fixed=[
 ('blocker','العنوان كان عبارة امتثال','كل صفحات المنتجات الـ27 كانت تفتح بـ«مناسب كي…» واسم المنتج مُنزّل إلى فقرة صغيرة. الآن لكل نمط عنوان مكتوب — «المساء يبدأ من الكرة الأولى» — وعبارة المكان عادت إلى مكانها الصحيح فوقه.'),
 ('blocker','قسم «متى لا يناسب» كان فارغاً','كان يعرض الجانب الإيجابي فقط على المنتجات الثلاثة: لا مفتاح ولا سلبية ولا سؤال شمس — أي أن الشيء الوحيد الذي يميّز المتجر كان إطاراً فارغاً. السبب أنه رُبط بحقل بيانات فارغ على 26 منتجاً. الآن يُشتقّ من الأزواج الأربعة المعتمدة ومن وصف المنتج نفسه.'),
 ('blocker','الجدول كان يبيع خياراً غير الذي اخترته','عند اختيار 11 متراً في الشاشة الأولى، كان الجدول يبقى على 5 أمتار وزره يضيف الخيار الخطأ إلى السلة — على الأنماط الثلاثة. الآن الشاشة والجدول والشريط السفلي يتفقون في الاتجاهين، والمعرّف الذي يصل السلة هو الذي اختاره المشتري.'),
 ('major','عمود «لماذا هذا الطول» كان فارغاً','ستة عشر سطراً مقتبساً من وصف كل منتج: ماذا يكفي كل طول أو كمية. هذا ما يحسم بين 9.5 و11 متراً.'),
 ('major','معرض «الليل» في مصباح الحائط كان نهارياً','صورة استوديو بيضاء وورقة مواصفات المورّد بأربع خانات. أُضيفت إلى قائمة المنع وبُدّلت الفهارس.'),
 ('major','النطاقات الرقمية كانت تُطبع مقلوبة','«5–22 متر» كانت تظهر «22–5» لغياب عازل اتجاه. أُنشئ عنصر مشترك يعالجها في كل الصفحة.'),
 ('major','زر الشراء كان 43 بكسل','تحت حد اللمس. صار 52، وأهداف اللمس الثانوية 44.'),
 ('major','الصفحات الثلاث كانت صفحة واحدة','نفس الإيقاع ونفس الأشكال الثمانية بنفس الارتفاعات. الآن لكل نمط شكل ضوء خاص: سلسلة معلّقة للغرلندة، وهالة للممر، وصفّ أعمدة للحائط.'),
]
tests=[('الشراء بلوحة المفاتيح وحدها','ست ضغطات Tab حتى الإضافة، والدرج يُفتح'),
 ('بدون JavaScript','كل سعر ظاهر، وكل صفّ في الجدول نموذج إرسال حقيقي، ولا صفحة سوداء'),
 ('تقليل الحركة','كل المصابيح مضاءة بلا أي انتقال'),
 ('عرض 320 بكسل','لا فيض أفقي ولا نص مقصوص'),
 ('بنية الصفحة','عنوان رئيسي واحد، وترتيب عناوين سليم، وARIA نظيفة على الجدول والمفتاح')]
rows=''.join(f'<tr><td><span class="sev sev--{s}">{"حاجب" if s=="blocker" else "كبير"}</span></td><td><b>{t}</b><p>{d}</p></td></tr>' for s,t,d in fixed)
tl=''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a,b in tests)
html=f'''<title>صفحة المنتج الجديدة</title>
<meta name="description" content="صفحة منتج ElmsNest الجديدة على ثيم التطوير: ما تغيّر، وما وجده النقد العدائي، وما ينتظر حكمك">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=IBM+Plex+Sans+Arabic:wght@300;400;500;600&display=swap">
<style>
:root{{--bg:#070b13;--bg2:#0d1524;--ink:#f4eee3;--ink2:#c9c4b8;--mute:#8f95a3;--gold:#e9b96e;--glow:#ffd394;--hair:rgba(244,238,227,.13);--bad:#f0a0a0;--warn:#f0c674;--ok:#8fd3a5;
--serif:"Amiri",serif;--sans:"IBM Plex Sans Arabic",system-ui,-apple-system,"Segoe UI",sans-serif}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-weight:300;font-size:16px;line-height:1.75;direction:rtl;-webkit-font-smoothing:antialiased}}
.wrap{{width:min(1140px,100% - 44px);margin-inline:auto}}
h1,h2,h3{{font-family:var(--serif);font-weight:700;line-height:1.15;margin:0;text-wrap:balance}}
h1{{font-size:clamp(36px,5.6vw,66px)}} h2{{font-size:clamp(26px,3.2vw,40px);margin-bottom:12px}} h3{{font-size:22px}}
p{{margin:0 0 13px;max-width:74ch}}
.eyebrow{{display:flex;align-items:center;gap:13px;font-size:12px;font-weight:500;letter-spacing:.14em;color:var(--gold);margin-bottom:13px}}
.eyebrow::before{{content:"";width:36px;height:1px;background:var(--gold);flex:none}}
header.top{{padding:66px 0 40px;position:relative;overflow:hidden}}
header.top::after{{content:"";position:absolute;inset-inline-start:-8%;top:-45%;width:66%;height:150%;background:radial-gradient(closest-side,rgba(255,211,148,.10),transparent 70%);pointer-events:none}}
.lede{{font-size:19.5px;color:var(--ink2);max-width:58ch;margin-top:18px;position:relative}}
.stat{{display:flex;flex-wrap:wrap;gap:14px 34px;margin-top:26px;font-size:14.5px;color:var(--mute)}}
.stat b{{color:var(--glow);font-family:var(--serif);font-size:22px;font-weight:700;margin-inline-end:6px;font-variant-numeric:tabular-nums}}
nav.toc{{position:sticky;top:0;z-index:9;background:rgba(7,11,19,.94);backdrop-filter:blur(10px);border-block:1px solid var(--hair);padding:11px 0}}
nav.toc ul{{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:2px 22px;font-size:14px}}
nav.toc a{{color:var(--ink2);text-decoration:none;padding:5px 0;border-bottom:1px solid transparent}}
nav.toc a:hover,nav.toc a:focus-visible{{color:var(--glow);border-color:var(--glow)}}
section{{padding:58px 0 26px;scroll-margin-top:62px}}
section+section{{border-top:1px solid var(--hair)}}
.ba{{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:24px}}
.ba figure{{margin:0}} .ba img{{width:100%;display:block;border:1px solid var(--hair)}}
.ba figcaption{{margin-top:10px;font-size:14px;color:var(--ink2)}}
.ba b{{display:block;font-family:var(--serif);font-size:19px;color:var(--ink);margin-bottom:3px}}
.ba .old b{{color:var(--mute)}}
.shot{{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:28px;align-items:start;margin-top:26px}}
.shot img{{width:100%;display:block;border:1px solid var(--hair)}}
.shot .txt b{{display:block;font-family:var(--serif);font-size:23px;margin-bottom:8px}}
.shot .txt p{{font-size:15px;color:var(--ink2)}}
.shot--m{{grid-template-columns:minmax(0,.62fr) minmax(0,1fr)}}
table{{border-collapse:collapse;width:100%;margin-top:22px}}
td{{vertical-align:top;padding:15px 0;border-top:1px solid var(--hair)}}
td:first-child{{width:78px}}
tr:last-child td{{border-bottom:1px solid var(--hair)}}
td b{{font-weight:600;font-size:16.5px}}
td p{{margin:5px 0 0;font-size:15px;color:var(--ink2)}}
.sev{{display:inline-block;font-size:11.5px;font-weight:500;padding:3px 9px;border-radius:999px;white-space:nowrap}}
.sev--blocker{{background:rgba(240,160,160,.14);color:var(--bad)}}
.sev--major{{background:rgba(240,198,116,.13);color:var(--warn)}}
ul.tests{{list-style:none;padding:0;margin:20px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0 30px}}
ul.tests li{{padding:14px 0;border-top:1px solid var(--hair);font-size:15px;color:var(--ink2);display:flex;gap:10px;align-items:baseline}}
ul.tests b{{color:var(--ink);font-weight:600;font-size:15.5px;flex:none}}
ul.tests li::before{{content:"✓";color:var(--ok);font-size:14px}}
.note{{border-inline-start:2px solid var(--gold);padding:18px 24px;background:var(--bg2);margin-top:22px;font-size:15.5px}}
.note p:last-child{{margin-bottom:0}}
ol.next{{counter-reset:n;list-style:none;padding:0;margin:22px 0 0}}
ol.next li{{counter-increment:n;display:grid;grid-template-columns:44px 1fr;gap:16px;padding:16px 0;border-top:1px solid var(--hair)}}
ol.next li:last-child{{border-bottom:1px solid var(--hair)}}
ol.next li::before{{content:counter(n,decimal-leading-zero);font-family:var(--serif);font-size:24px;color:var(--gold);font-variant-numeric:tabular-nums}}
ol.next b{{font-weight:600}} ol.next p{{margin:4px 0 0;font-size:15px;color:var(--ink2)}}
code{{font-family:ui-monospace,Menlo,monospace;font-size:.86em;direction:ltr;unicode-bidi:isolate;background:rgba(244,238,227,.07);padding:1px 6px;color:var(--ink2)}}
footer{{padding:38px 0 60px;color:var(--mute);font-size:13.5px;border-top:1px solid var(--hair);margin-top:32px}}
@media (max-width:820px){{.ba,.shot,.shot--m{{grid-template-columns:1fr}}}}
</style>
<header class="top"><div class="wrap">
<p class="eyebrow">ElmsNest · صفحة المنتج · بُنيت ونُقدت وأُصلحت · ثيم التطوير 154726400174</p>
<h1>صفحة المنتج الجديدة، حيّة على ثيم التطوير.</h1>
<p class="lede">ثمانية أقسام جديدة حلّت محل تصميم PDP السابق. بعد البناء دقّقها أربعة نقّاد عدائيين على الرندر الحقيقي — أحدهم نفّذ عملية شراء كاملة من هاتفه — فوجدوا ثلاثة عيوب حاجبة وسبعة عشر كبيراً. أُغلقت كلها وأُعيد النشر والقياس.</p>
<div class="stat"><span><b>8</b>أقسام</span><span><b>3</b>عيوب حاجبة أُغلقت</span><span><b>8,492</b>بكسل بدل 9,599</span><span><b>0</b>أخطاء Liquid</span><span><b>52</b>بكسل زر الشراء</span></div>
</div></header>
<nav class="toc"><div class="wrap"><ul><li><a href="#ba">قبل وبعد</a></li><li><a href="#sell">شاشة البيع</a></li><li><a href="#no">«متى لا يناسب»</a></li><li><a href="#ledger">الجدول</a></li><li><a href="#wall">الصدق في الاتجاه الآخر</a></li><li><a href="#fixed">ما أصلحه النقد</a></li><li><a href="#next">التالي</a></li></ul></div></nav>
<main>
<section id="ba"><div class="wrap"><p class="eyebrow">01 · قبل وبعد</p><h2>نفس المنتج، نفس الشاشة الأولى</h2>
<div class="ba">
<figure class="old"><img src="{img('before')}" alt="التصميم السابق: كريمي مع صناديق"><figcaption><b>قبل — «PDP Design v2»</b>أرضية كريمية، خط Assistant، صناديق، منتقي خيارات بلا سعر، وقائمة رأس غير مرئية.</figcaption></figure>
<figure><img src="{img('after')}" alt="التصميم الجديد: ليلي مع صورة المنتج"><figcaption><b>بعد</b>صورة ليلية للمنتج نفسه، عنوان مكتوب بخط Frank Ruhl Libre، السعر متوهّجاً، وزر شراء واضح — على نظام تصميم الصفحة الرئيسية.</figcaption></figure>
</div></div></section>
<section id="sell"><div class="wrap"><p class="eyebrow">02 · الشاشة الأولى على الهاتف</p><h2>كل قرار الشراء بلا تمرير واحد</h2>
<div class="shot shot--m"><img src="{img('mobile')}" alt="الشاشة الأولى على هاتف 390 بكسل">
<div class="txt"><b>سبعة عناصر فوق 844 بكسل</b>
<p>المكان والعبارة المعتمدة، عنوان مكتوب («المساء يبدأ من الكرة الأولى»)، اسم المنتج، اللون كاختيار واحد هادئ، السعر 89.90 ₪ مع شرح صادق لمداه وأن اللون لا يغيّره، زر «إضافة للسلة» بحافة سفلية عند 555 بكسل، ورابط <b style="display:inline;font-family:inherit;font-size:inherit">«لمن هذا لا يناسب»</b> بجانب الزر مباشرة — السلبية معروضة في لحظة الالتزام.</p>
<p>ثم الأرقام الأربعة في سطر، وخطوة إرسال صورة المكان، وبداية جدول الأطوال الستة بأسعارها.</p></div></div></div></section>
<section id="no"><div class="wrap"><p class="eyebrow">03 · الفارق الذي لا يُنسخ</p><h2>مفتاح يُطفئ الضوء فعلاً</h2>
<p>هذا القسم كان أخطر ما وجده النقد: كان يعرض الجانب الإيجابي فقط، فيصير الشيء الوحيد الذي يميّز متجرك إطاراً فارغاً. الآن يعمل.</p>
<div class="shot"><img src="{img('fit')}" alt="قسم متى يناسب ومتى لا: مفتاح بين الجانبين وسلسلة أنوار تنطفئ">
<div class="txt"><b>«مناسب كي تصنع جوّاً» ⟷ «لا يناسب حين يلزم ضوء قوي — ليست هذه غايتها»</b>
<p>الزوج المعتمد حرفياً من صفحاتك المنشورة، لا جملة جديدة. تُحوّل المفتاح فتنطفئ سلسلة الأنوار تحته وتظهر «لم تُضِئ. هذه هي النقطة».</p>
<p>وتحته سؤال المشتري عن مكانه: «كم شمساً يأخذ المكان في النهار؟» بجوابيه — فيستبعد نفسه قبل أن يدفع، بدل أن يكتشف بعد الاستلام.</p></div></div></div></section>
<section id="ledger"><div class="wrap"><p class="eyebrow">04 · القرار</p><h2>أربعة وعشرون خياراً تصير قراراً واحداً</h2>
<div class="shot"><img src="{img('ledger')}" alt="جدول الأطوال بأسعارها وسعر المتر ومعنى كل طول">
<div class="txt"><b>كل طول بسعره وسعر متره ومعناه وزر إضافة خاص به</b>
<p>سعر المتر يجعل المقارنة فورية: 17.98 ₪ للمتر في الأقصر مقابل 8.18 ₪ في الأطول. ومعنى كل صفّ مقتبس من وصف المنتج نفسه، وهو ما يحسم فعلاً بين 9.5 و11 متراً.</p>
<p>ولأن كل صفّ نموذج إرسال مستقل، الجدول يعمل بالكامل حتى بلا JavaScript.</p></div></div></div></section>
<section id="wall"><div class="wrap"><p class="eyebrow">05 · الصدق في الاتجاه الآخر</p><h2>حين لا يوجد ما يُقال، لا يُقال شيء</h2>
<div class="shot"><img src="{img('wall')}" alt="صفحة مصباح الحائط الكهربائي">
<div class="txt"><b>مصباح الحائط الكهربائي لا يحمل جملة شمسية واحدة</b>
<p>التصميم السابق كان يطبع «التركيب بلا أسلاك وبلا كهربائي» و«اختر مكاناً يأخذ شمساً» على مصابيح تعمل بالكهرباء. الآن فرع مصدر الطاقة يمنع ذلك.</p>
<p>وقسم «متى لا يناسب» يبقى في وضع الاختيار على هذا المنتج ولا يطبع سلبية — لأن أياً من الأزواج الأربعة المعتمدة ليس صحيحاً حرفياً لمصباح كهربائي. الوعد نفسه محفوظ في الاتجاهين.</p></div></div></div></section>
<section id="fixed"><div class="wrap"><p class="eyebrow">06 · النقد العدائي</p><h2>ما وجده النقّاد الأربعة، وما أُصلح</h2>
<p>مدير إبداعي، ومتسوّقة إسرائيلية نفّذت الشراء فعلاً من هاتفها على المنتجات الثلاثة، ومصمم طباعة عبرية، ومهندس QA. هذه العيوب الحاجبة والكبيرة، وكلها مُغلقة ومُعاد قياسها.</p>
<table><tbody>{rows}</tbody></table>
<div class="note"><p><b>وما اجتازته الصفحة من اختبارات:</b></p>
<ul class="tests">{tl}</ul></div>
</div></section>
<section id="next"><div class="wrap"><p class="eyebrow">07 · التالي</p><h2>ما ينتظر كلمتك</h2>
<div class="shot"><img src="{img('close')}" alt="الشاشة الأخيرة: صورة ملء العرض واقتباس من نحن">
<div class="txt"><b>الصفحة تُختم بصورة ملء العرض واقتباس «من نحن»</b><p>«حين لا يكون المعلومة مؤكّدة، لا يجوز عرضها كحقيقة» — الجملة التي تحكم كل ما كُتب في الصفحة.</p></div></div>
<ol class="next">
<li><div><b>حكمك على الصفحة</b><p>عايِنها بنفسك على <code>elmsnest.com/products/solar-crystal-ball-string-lights?preview_theme_id=154726400174</code> — ومثلها لأي منتج. لم يُنشر شيء على المتجر الحي.</p></div></li>
<li><div><b>جدول المواصفات (27 منتجاً)</b><p>جاهز في <code>METAFIELD-SHEET.md</code> وينتظر موافقتك، لأن كتابته تغيّر صفحات المنتجات الحية أيضاً. أربعة بنود تحتاج قرارك: مصدر الطاقة لثلاثة منتجات، وواط الپروجكتور، وأربع قيم «لا يناسب»، وهل «للاستعمال الداخلي» يصير زوجاً معتمداً خامساً.</p></div></li>
<li><div><b>ثم الكولكشن</b><p>بطاقة المنتج التي صُمّمت داخل هذه الصفحة تصبح بطاقة الكتالوج، فتبدأ الجولة التالية ونصف عملها جاهز.</p></div></li>
</ol></div></section>
</main>
<footer><div class="wrap"><p>المصادر في الفرع <code>claude/design-sidebar-pages-3991tn</code>: تقرير البناء <code>brief/side-pages/pdp/BUILD-REPORT.md</code> · نقد النقّاد الأربعة <code>CRITIQUE-*.md</code> · المواصفة <code>WINNING-SPEC.md</code> · الحكم <code>RULING.md</code>. ثيم التطوير غير منشور والمتجر الحي لم يُمس.</p></div></footer>
'''
open(OUT,'w',encoding='utf-8').write(html)
print('written',os.path.getsize(OUT)//1024,'KB')
