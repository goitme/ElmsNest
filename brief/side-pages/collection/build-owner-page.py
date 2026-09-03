# -*- coding: utf-8 -*-
import base64,os
IMG='/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/report4-img'
OUT='/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/collection-built.html'
def img(n): return 'data:image/jpeg;base64,'+base64.b64encode(open(f'{IMG}/{n}.jpg','rb').read()).decode()
fixed=[
 ('blocker','بطاقة المصباح كانت تطبع فوق العنوان','على شاشة آيفون الصغيرة (390×664) تتراكب البطاقة المثبَّتة مع اسم الكولكشن فيصيران نصاً غير مقروء. وصفه مهندس الاختبار بأنه «الشيء الوحيد الذي يرفضه المالك بمجرد النظر». الآن مقيس على 25 حالة: لا تراكب في أي منها، وأقل هامش 24 بكسل.'),
 ('major','فكرة الصفحة كانت مُطفأة عند الوصول','في الحالة الافتراضية كانت ثلاثة صفوف من أربعة تطبع العبارة نفسها «من 89.90 ₪»، وسعر المتر — الرقم الذي لا يطبعه منافس — غائباً. الآن يظهر عند «الكل» أيضاً: 17.98 · 59.93 · 12.84 · 27.98، أربعة أرقام متمايزة قبل أي ضغطة.'),
 ('major','جملة مولَّدة حسابياً في صندوق مصمت','المكان الوحيد المخصّص لصوت إنسان كان يحمل جملة يبنيها الكود من أصغر سعر وأكبره، داخل الصندوق المعتم الوحيد في الصفحة. حُذفت من المصدر نهائياً، وحلّت محلها جملة مكتوبة، والصندوق صار خطاً ذهبياً.'),
 ('major','صور استوديو كريمية رغم منعها','ثلاث بطاقات كانت تعرض صوراً نهارية على خلفية كريمية، إحداها أكبر صورة في صفحة الكتالوج كلها. تبيّن أن حجاب التعتيم كان مكتوباً على الطبقة نفسها التي تملكها النواة للهالة، فلم يُرسم قط. المتحقّق قاس 54 صندوق صورة في أسطع حالاتها: صفر كريمي في جميعها.'),
 ('major','المصباح غير المضاء كان يبدو صورة معطوبة','نفس ملف الصورة كان يظهر مرة مضيئاً ومرة كبقعة بنية بلا تفاصيل، فوق منتج قابل للشراء. رُفعت أرضية الإضاءة على صفحة الكولكشن وحدها؛ الرئيسية وصفحة المنتج بقيتا كما هما.'),
 ('major','قاعدة CSS تكسر آخر كلمة من كل عنوان','أربع كلمات في ورقة الأنماط كانت تُنزل الكلمة الأخيرة من كل عنوان كولكشن إلى سطر مستقل — ومنها يُتم «ניידת» على سطر ثالث. أُزيلت، فعاد التوازن التلقائي للأسطر.'),
 ('major','فقرة بعرض 76 حرفاً في نظام يحدّ 38','الفقرة الوحيدة الجارية في الصفحة كانت ضعف العرض المسموح. صارت 46 حرفاً في السطر.'),
 ('major','أسماء المنتجات 11 بكسل ومقصوصة','اسم على البطاقة كان يُعرض 31٪ منه فقط. صار 13 بكسل بلا قصّ، وبثلاث كلمات أولى من اسم المنتج.'),
]
checks=[('التراكب على 5 صفحات × 4 أحجام','لا شيء في العشرين'),
 ('سطر التضييق','44 بكسل وداخل الطيّة في العشرين'),
 ('الفيض الأفقي','لا شيء'),
 ('أخطاء Liquid','صفر في المرايا الخمس'),
 ('صفحة المنتج لم تتغيّر','فرق مطلق صفر على 48 مليون بكسل'),
 ('التضييق بلا JavaScript','مطابق حرفياً للنسخة العاملة')]
rows=''.join(f'<tr><td><span class="sev sev--{s}">{"حاجب" if s=="blocker" else "كبير"}</span></td><td><b>{t}</b><p>{d}</p></td></tr>' for s,t,d in fixed)
ch=''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a,b in checks)
html=f'''<title>صفحة الكولكشن الجديدة</title>
<meta name="description" content="صفحة الكولكشن الجديدة على ثيم التطوير: المسطرة التي تضيّق الكتالوج، وما وجده النقد العدائي، والعيب الذي قبلته صراحةً">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=IBM+Plex+Sans+Arabic:wght@300;400;500;600&display=swap">
<style>
:root{{--bg:#070b13;--bg2:#0d1524;--ink:#f4eee3;--ink2:#c9c4b8;--mute:#8f95a3;--gold:#e9b96e;--glow:#ffd394;--hair:rgba(244,238,227,.13);--bad:#f0a0a0;--warn:#f0c674;--ok:#8fd3a5;
--serif:"Amiri",serif;--sans:"IBM Plex Sans Arabic",system-ui,-apple-system,"Segoe UI",sans-serif}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-weight:300;font-size:16px;line-height:1.75;direction:rtl;-webkit-font-smoothing:antialiased}}
.wrap{{width:min(1140px,100% - 44px);margin-inline:auto}}
h1,h2,h3{{font-family:var(--serif);font-weight:700;line-height:1.15;margin:0;text-wrap:balance}}
h1{{font-size:clamp(36px,5.6vw,64px)}} h2{{font-size:clamp(26px,3.2vw,40px);margin-bottom:12px}}
p{{margin:0 0 13px;max-width:74ch}}
.eyebrow{{display:flex;align-items:center;gap:13px;font-size:12px;font-weight:500;letter-spacing:.14em;color:var(--gold);margin-bottom:13px}}
.eyebrow::before{{content:"";width:36px;height:1px;background:var(--gold);flex:none}}
header.top{{padding:66px 0 40px;position:relative;overflow:hidden}}
header.top::after{{content:"";position:absolute;inset-inline-start:-8%;top:-45%;width:66%;height:150%;background:radial-gradient(closest-side,rgba(255,211,148,.10),transparent 70%);pointer-events:none}}
.lede{{font-size:19.5px;color:var(--ink2);max-width:58ch;margin-top:18px;position:relative}}
.stat{{display:flex;flex-wrap:wrap;gap:14px 32px;margin-top:26px;font-size:14.5px;color:var(--mute)}}
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
.shot--m{{grid-template-columns:minmax(0,.6fr) minmax(0,1fr)}}
table{{border-collapse:collapse;width:100%;margin-top:22px}}
td{{vertical-align:top;padding:15px 0;border-top:1px solid var(--hair)}}
td:first-child{{width:78px}} tr:last-child td{{border-bottom:1px solid var(--hair)}}
td b{{font-weight:600;font-size:16.5px}} td p{{margin:5px 0 0;font-size:15px;color:var(--ink2)}}
.sev{{display:inline-block;font-size:11.5px;font-weight:500;padding:3px 9px;border-radius:999px;white-space:nowrap}}
.sev--blocker{{background:rgba(240,160,160,.14);color:var(--bad)}}
.sev--major{{background:rgba(240,198,116,.13);color:var(--warn)}}
ul.checks{{list-style:none;padding:0;margin:20px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:0 30px}}
ul.checks li{{padding:13px 0;border-top:1px solid var(--hair);font-size:15px;color:var(--ink2);display:flex;gap:10px;align-items:baseline}}
ul.checks b{{color:var(--ink);font-weight:600;font-size:15.5px;flex:none}}
ul.checks li::before{{content:"✓";color:var(--ok);font-size:14px}}
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
<p class="eyebrow">ElmsNest · صفحة الكولكشن · خمسة عناوين · ثيم التطوير 154726400174</p>
<h1>الكتالوج صار يُقاس بالوحدة التي يفكّر بها المشتري.</h1>
<p class="lede">سبعة أقسام جديدة حلّت محل صفحة كتالوج Kalles. بعد البناء دقّقها أربعة نقّاد عدائيين فوجدوا 42 ملاحظة، ثم راجع الإصلاحَ متحقّقٌ مستقل أعاد كل القياسات بنفسه ولم يثق بمرايا المُصلِح.</p>
<div class="stat"><span><b>5</b>عناوين</span><span><b>42</b>ملاحظة</span><span><b>24</b>أُغلقت بأدلة</span><span><b>0</b>أخطاء Liquid</span><span><b>20/20</b>حالة قياس نظيفة</span></div>
</div></header>
<nav class="toc"><div class="wrap"><ul><li><a href="#ba">قبل وبعد</a></li><li><a href="#ruler">المسطرة</a></li><li><a href="#fold">الشاشة الأولى</a></li><li><a href="#glyph">حين لا توجد صورة</a></li><li><a href="#fixed">ما أصلحه النقد</a></li><li><a href="#open">عيب قبلته</a></li><li><a href="#next">التالي</a></li></ul></div></nav>
<main>
<section id="ba"><div class="wrap"><p class="eyebrow">01 · قبل وبعد</p><h2>صفحة الكتالوج، نفس العنوان</h2>
<div class="ba">
<figure class="old"><img src="{img('before')}" alt="التصميم السابق: كتالوج Kalles كريمي"><figcaption><b>قبل</b>أرضية كريمية، شريط بنّي، شريط أدوات بستة أيقونات شبكة وفلتر إنجليزي، وبطاقات ثلثا صورها ملصقات بنص مطبوع. القائمة العلوية غير مرئية.</figcaption></figure>
<figure><img src="{img('after')}" alt="التصميم الجديد: مشهد ليلي مع فهرس الأماكن"><figcaption><b>بعد</b>مشهد ليلي، عدد المنتجات والخيارات والمدى السعري محسوبة، وفهرس بالأماكن الأربعة — كلٌّ بعدده ومداه وأسماء أوائل منتجاته.</figcaption></figure>
</div></div></section>
<section id="ruler"><div class="wrap"><p class="eyebrow">02 · الفكرة</p><h2>سبعة منتجات و105 خيارات، وقرار واحد</h2>
<div class="shot"><img src="{img('ruler')}" alt="مسطرة الأمتار: كل منتج صفّ عليه نقاط مضيئة عند أطواله الحقيقية">
<div class="txt"><b>كل منتج مسطرة، وكل نقطة مضيئة طول موجود فعلاً</b>
<p>تختار «6 أمتار» فينكمش كل صفّ من مدى إلى جواب واحد: 6.5 م بـ89.90 · 6 م بـ119.90 · 7 م بـ89.90 · 8 م بـ179.90 — ومعها سعر المتر، فيظهر الأوفر بلا حساب.</p>
<p>والمنتج الذي لا يصل إلى الطول المطلوب لا يختفي: يخفت ويكتب إلى أين يصل. <b style="display:inline;font-family:inherit;font-size:inherit">والأداة كلها CSS خالص</b> — تعمل بنتيجة مطابقة حرفياً مع تعطيل JavaScript، لأن المحطة ملصق فوق زر راديو أصلي.</p></div></div></div></section>
<section id="fold"><div class="wrap"><p class="eyebrow">03 · الشاشة الأولى</p><h2>أين أنا، وماذا يوجد، وبكم</h2>
<div class="shot shot--m"><img src="{img('mobile')}" alt="الشاشة الأولى على هاتف">
<div class="txt"><b>أخطر عيب في الجرد كان هنا</b>
<p>أربع من خمس صفحات لم تكن تعرض سعراً ولا منتجاً في الشاشة الأولى — لافتة وفقرة وشريط أدوات فقط. الآن الخمس جميعاً تعرض المكان، والعبارة المعتمدة، والأعداد المحسوبة، وسطر «كم ضوءاً يحتاج المكان؟» الذي يقود إلى المسطرة، ومنتجاً حقيقياً بسعره وسعر متره وطريق شرائه.</p></div></div></div></section>
<section id="glyph"><div class="wrap"><p class="eyebrow">04 · الصدق</p><h2>خمسة عشر منتجاً بلا صورة نظيفة</h2>
<div class="shot"><img src="{img('glyph')}" alt="لوحة رسم بدل صورة المنتج">
<div class="txt"><b>«رسم · لا يوجد تصوير نظيف»</b>
<p>صور هذه المنتجات الرئيسية ملصقات تسويقية بنص عبري مطبوع وادعاءات رقمية، وإحداها تحمل علامة طرف ثالث. بدل عرضها أو ترك فراغ، ترسم الصفحة المصباح بخط واحد داخل هالة وتكتب صراحة أنه رسم.</p>
<p>على صفحة الأضواء الكاشفة ستة من ستة كذلك — وهي تُقرأ كخيار مقصود لا كعطل.</p></div></div></div></section>
<section id="fixed"><div class="wrap"><p class="eyebrow">05 · النقد العدائي</p><h2>ما وجده النقّاد الأربعة، وما أُصلح</h2>
<p>مدير إبداعي، ومتسوّقة نفّذت الشراء من هاتفها، ومصمم طباعة عبرية، ومهندس اختبار. ثم متحقّق مستقل أعاد كل قياس بنفسه — ورفض الوثوق بمرايا سابقة للنشر، بعد أن أنتجت ملاحظة خاطئة واحدة.</p>
<table><tbody>{rows}</tbody></table>
<div class="note"><p><b>وما تحقّق منه المتحقّق المستقل بقياساته:</b></p><ul class="checks">{ch}</ul></div>
</div></section>
<section id="open"><div class="wrap"><p class="eyebrow">06 · شفافية</p><h2>عيب واحد قبلته، ولم أُغلقه</h2>
<div class="note"><p><b>على شاشة بعرض 320 بكسل يقع زر الشراء تحت الطيّة بـ26 إلى 43 بكسلاً.</b> سببه إصلاح العيب الحاجب نفسه: حجز مساحة للبطاقة كي لا تطبع فوق العنوان دفع ما تحتها للأسفل.</p>
<p>البدائل الثلاثة كلها أغلى: اثنان يُعيدان التراكب، والثالث يحذف سعر المتر من بطاقة الشاشة الأولى — أقوى أداة بيع في الصفحة — على كل هاتف بعرض 360 فأقل، مقابل 40 بكسلاً على جهاز من 2016، ولا يكفي حتى لسدّ العجز.</p>
<p>على 320 يرى الزائر كل شيء ويمرّر 43 بكسلاً ليصل الزر. والخط الذي لا يُتجاوز مسجَّل كالتزام: <b>360×640 يجب أن يبقى داخل الطيّة</b>، وأي تغيير يُخرجه ارتداد.</p>
<p>ويستحق الذكر أن الصفحة قبل هذه الجولة كانت «تنجح» على 320 لأن البطاقة كانت تطبع فوق العنوان — أي بفضل العيب لا رغمه.</p></div></div></section>
<section id="next"><div class="wrap"><p class="eyebrow">07 · التالي</p><h2>ما ينتظر كلمتك</h2>
<ol class="next">
<li><div><b>عايِن الصفحات الخمس</b><p><code>elmsnest.com/collections/all?preview_theme_id=154726400174</code> — ومثلها لأي كولكشن. لم يُنشر شيء على المتجر الحي.</p></div></li>
<li><div><b>حكمك على صفحة المنتج وعلى هذه</b><p>كلتاهما مبنية ومنقودة ومُصلَحة وتنتظر رأيك.</p></div></li>
<li><div><b>جدول المواصفات (27 منتجاً)</b><p>جاهز وينتظر موافقتك، لأن كتابته تُغيّر صفحات المنتجات الحية أيضاً. أربعة بنود تحتاج قرارك.</p></div></li>
<li><div><b>ثم السلة والدرج، فالبحث و404، فصفحات المحتوى</b><p>بطاقة المنتج والنواة المشتركة جاهزتان، فكل جولة تالية أقصر من سابقتها.</p></div></li>
</ol></div></section>
</main>
<footer><div class="wrap"><p>المصادر في الفرع <code>claude/design-sidebar-pages-3991tn</code>: تقرير الإصلاح <code>brief/side-pages/collection/FIX-REPORT.md</code> · النقد <code>CRITIQUE-{{lead,creative,typographer,qa}}.md</code> · المواصفة <code>WINNING-SPEC.md</code> · الموجز <code>BRIEF.md</code>. ثيم التطوير غير منشور والمتجر الحي لم يُمس.</p></div></footer>
'''
open(OUT,'w',encoding='utf-8').write(html); print('written',os.path.getsize(OUT)//1024,'KB')
