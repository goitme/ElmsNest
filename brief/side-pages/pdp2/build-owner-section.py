#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Owner-page section for the PRODUCT-PAGE round 2 (Arabic). Writes pdp2/OWNER-SECTION.json ({"html": ...}) which
simplify/build-owner-page.py splices into the owner page (same Artifact URL), after the home round-2 section.
Photographs = the real render of the dev theme (pdp2/verify*/ from shoot-sections.js and pdp2/verify-after/ from the
verifier), embedded as JPEG data URIs. The critique paragraph comes from pdp2/critique/SUMMARY.json when it exists
(written by the lead after the skeptics), else an honest placeholder."""
import base64, io, json, os
from PIL import Image
P = '/home/user/ElmsNest/brief/side-pages/pdp2'; V = f'{P}/verify'; VA = f'{P}/verify-after'
CRIT = json.load(open(f'{P}/critique/SUMMARY.json', encoding='utf-8')) if os.path.exists(f'{P}/critique/SUMMARY.json') else None
A = json.load(open(f'{VA}/verify.json'))
B = json.load(open(f'{P}/verify-before/verify.json')) if os.path.exists(f'{P}/verify-before/verify.json') else {}
SIMB = json.load(open('/home/user/ElmsNest/brief/side-pages/simplify/verify-after/verify.json'))
def jpg(path, width=390, q=80):
    if not os.path.exists(path): return ''
    im = Image.open(path).convert('RGB')
    if im.width > width: im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
def scr(d, k): return d.get(k, {}).get('screens', '—')
def secs(k):
    s = {x['section']: x for x in A.get(k, {}).get('pdpSections', [])}
    return s.get('ens-pdp-scene', {}).get('h', '—'), s.get('ens-pdp-dusk', {}).get('h', '—')
pages = [('pdp-path', 'مصباح الممرّ من الستانلس (شمسي، خيار واحد)', SIMB), ('pdp-rope', 'حبل الإضاءة الشمسي (شمسي، 16 خياراً)', SIMB), ('pdp-deck', 'إضاءة الدرج الشمسية (شمسي، بلا إطار نظيف)', SIMB), ('pdp-wall', 'مصباح الجدار المقاوم للماء (كهرباء، 8 خيارات)', B), ('pdp-flood', 'الكشّاف الشمسي (شمسي، بلا إطار نظيف)', B)]
rows = ''.join(f'<tr><td>{t}</td><td dir="ltr">{scr(before, k + "-m-js")}</td><td dir="ltr"><b>{scr(A, k + "-m-js")}</b></td><td dir="ltr">{secs(k + "-m-js")[0]} / {secs(k + "-m-js")[1]}</td></tr>' for k, t, before in pages)
phone = [(f'{V}/scene-m.png', 'בלילה, על השביל', 'مصباح الممرّ: صورته السادسة من معرضه بعرض الشاشة (440 بكسل)، ثم عنوان المكان وسطر واحد ورابط الدليل — على الأرضية الليلية، لا فوق الصورة.'),
         (f'{P}/verify-wall/scene-m.png', 'בלילה, על הקיר', 'مصباح الجدار (كهرباء): صورته السادسة، والسطر «אור על הקיר, בדיוק בנקודה שבחרתם.». لا سطر شمسي هنا: البوابة تعرف أنه ليس شمسياً.'),
         (f'{P}/verify-flood/scene-m-viewport.png', 'בלילה, בגינה', 'الكشّاف: لا إطار نظيف له في معرضه، فالقسم يعرض النصّ وحده ثم صفّ «כשמחשיך» ثم الأرقام. لا صورة منتج آخر — هذا خيارك (انظر الملاحظات).'),
         (f'{V}/dusk-m.png', 'כשמחשיך', 'صفّ واحد على خطّ رفيع للمنتجات الشمسية فقط: «نهاراً يجمع اللوح الشمس، وهذا ما يضيء ليلاً. شمس أكثر نهاراً، ضوء أكثر ليلاً.»')]
phone_html = ''.join(f'<figure><img src="{jpg(p)}" alt="" loading="lazy"><figcaption><b dir="rtl">{t}</b>{d}</figcaption></figure>' for p, t, d in phone)
wide = [(f'{V}/scene-d.png', 'القسم نفسه على شاشة 1366: الصورة 560 بكسل بعرض الشاشة، والعنوان على اليمين والسطر والرابط على اليسار — الشبكة نفسها التي يستعملها قسم الأرقام تحته.')]
wide_html = ''.join(f'<figure class="wide"><img src="{jpg(p, 1140, 74)}" alt="" loading="lazy"><figcaption>{d}</figcaption></figure>' for p, d in wide)
full_a = jpg(f'{VA}/pdp-path-m-js-full.png'); full_b = jpg(f'{VA}/pdp-flood-m-js-full.png')
own = [('stainless', 'stainless-steel-solar-path-light-ip65', '6', 'كاملة'), ('powerful', 'powerful-solar-garden-light', '4', 'قصّ الأسفل (كان فيه سطر «מתאים לגינה»)'),
       ('rope', 'solar-rope-string-lights', '3', 'قصّ الأعلى (شارة IP65)'), ('crystal', 'solar-crystal-ball-string-lights', '3', 'كاملة'), ('edison', 'solar-edison-string-lights', '4', 'كاملة'),
       ('firefly', 'solar-firefly-garden-lights', '4', 'كاملة'), ('birch', 'lighted-birch-branches-20-led', '4', 'كاملة (داخل البيت؛ العنوان «בערב, בבית»)'),
       ('bidirectional', 'outdoor-bidirectional-led-wall-light-ip65', '6', 'كاملة'), ('waterproof-wall', 'waterproof-led-wall-light-ip65-6w-12w', '6', 'كاملة'),
       ('wall-indoor-outdoor', 'modern-led-wall-light-indoor-outdoor', '5', 'كاملة (جدار استوديو، لكنه منتجك)'), ('wall-6w', 'modern-led-wall-light-6w-up-down', '7', 'كاملة (الأصل 1000 بكسل، أنعم من الباقي)'),
       ('dual-head', 'dual-head-garden-light-10w-ip65', '5', 'قصّ اليمين (لافتة LUMIÈRE أجنبية خارج الملف)'), ('modern-path', 'modern-solar-path-lights-set', '3', 'شريط أوسط (عنوان فوق، أيقونات تحت)'),
       ('lantern9', 'solar-garden-lantern-9-led', '6', 'شريط أوسط (عنوان فوق، أيقونات تحت)'), ('warm-step', 'warm-solar-step-deck-lights', '2', 'قصّ اليسار (عنوان وعمود أيقونات)')]
src_rows = ''.join(f'<tr><td dir="ltr" style="font-family:ui-monospace,monospace;font-size:13px">{h}</td><td dir="ltr" style="font-size:13px">ens-pdp-{a}.jpg</td><td dir="ltr">{n}</td><td>{c}</td></tr>' for a, h, n, c in own)
nophoto = ['magnetic-rechargeable-touch-wall-light', 'solar-wall-light-motion-sensor-ip65', 'waterproof-solar-deck-step-lights', 'retro-solar-path-lights-set', 'swaying-solar-path-lights-ip65', 'modern-led-bollard-light-5w-ip65', 'solar-garden-spotlight-52-led', 'solar-security-light-100-led', 'solar-floodlight-ip67-remote-timer', 'rechargeable-telescopic-camping-lantern', 'led-globe-string-lights', 'decorative-led-net-lights']
nophoto_html = '، '.join(f'<span dir="ltr" style="font-family:ui-monospace,monospace;font-size:12.5px">{h}</span>' for h in nophoto)
copy = [('בלילה, על השביל · בלילה, על הקיר · בלילה, בגינה · בלילה, במרפסת', 'عنوان القسم حسب الكولكشن (كلمة المكان المرخّصة نفسها). لأغصان البتولا داخل البيت: «בערב, בבית».'),
        ('אור נמוך, קרוב לאדמה, שמלווה את הדרך.', 'سطر عائلة الممرّ: شكل الضوء لا مواصفاته — لا مدى، لا ساعات، لا لومن.'),
        ('אור על הקיר, בדיוק בנקודה שבחרתם.', 'سطر عائلة الجدار: مصباح الجدار يضيء الجدار الذي ركّبتَه عليه.'),
        ('אור מכוון אל מה שרוצים לראות בלילה.', 'سطر عائلة الحديقة (سبوت، كشّاف، إضاءة أمان): ضوء موجَّه — صحيح للثلاثة، ولا يناقض «מאיר רחב» في وصف الكشّاف.'),
        ('הרבה נקודות אור קטנות במקום מנורה אחת. אור שיושבים בו.', 'سطر عائلة الشرفة (الجرلندات والديكور).'),
        ('למדריך לבחירת תאורה ←', 'رابط الدليل — الوحيد في صفحة المنتج (لم يكن فيها رابط دليل من قبل).'),
        ('כשמחשיך', 'عنوان الصفّ الشمسي.'),
        ('ביום הפאנל אוסף שמש, וזה מה שמאיר בלילה. · יותר שמש ביום, יותר אור בלילה.', 'الجملتان — حقيقة عامة عن الشمس بلا أرقام. تعمّدتُ ألا أقول «يشتعل وحده»: الكشّاف بريموت وتايمر، وإضاءة الأمان بحسّاس حركة.'),
        ('בתמונה: {שם המוצר}', 'سطر الكرديت — يظهر فقط إن شغّلتَ خيار «صورة الكولكشن» (مطفأ افتراضياً).')]
copy_html = ''.join(f'<li><b dir="rtl" lang="he">{he}</b><span class="muted"> — {ar}</span></li>' for he, ar in copy)
crit_html = CRIT['html'] if CRIT else '<p class="muted">النقد العدائي على اللقطات الحقيقية يعمل الآن (خمس عدسات: مشترٍ، أنت، حارس الصدق، مصمّم، مهندس؛ ومشكّك على كل ملاحظة). يُلحق هنا عند اكتماله.</p>'
html = f'''<section id="pdp2"><div class="wrap">
<p class="eyebrow">صفحة المنتج · الجولة الثانية</p><h2>قسمان بالصور على صفحة المنتج، مضبوطان لصفحة بيع</h2>
<blockquote>«بعدها ابداء في صفحة المنتج بنفس الطلب لكن زبطها اكثر لانه صفحة منتج صفحة بيع»<small>طلبك، 2026-09-06</small></blockquote>
<p>الطلب نفسه، لكن صفحة المنتج صفحة بيع، فالضبط كان هكذا: <b>لا شيء بين المعرض وزرّ الشراء</b>؛ القسمان يأتيان بعد الزرّ مباشرة وقبل الأرقام. <b>الصورة هي صورة منتجك أنت</b> — إطار من معرض المنتج نفسه، لا صورة منتج آخر ولا صورة من الإنترنت — لأن أي صورة على صفحة منتج تُقرأ على أنها «هذا المنتج». <b>كل سطر يخدم قرار الشراء</b>: كيف يبدو في مكانه ليلاً، ماذا يحدث عند الغروب (للشمسي فقط)، وأين يتأكّد قبل أن يطلب. ولا شيء يُقال مرتين: لا سعر ثانٍ، لا زرّ ثانٍ، لا شروط ثانية، لا «לא מתאים» ثانية.</p>
<p>خمسة مفاهيم رُسمت لثلاثة منتجات نموذجية (ممرّ شمسي بصور نظيفة · جدار كهربائي بصورة واحدة · كشّاف شمسي بلا صورة نظيفة) وحُكم عليها من اللقطات: <span dir="ltr">one 49.75 · scene 49.25 · places 42.5 · checks 36.75 · dusk 36.25</span> — تعادل في القمة، فبُني من الاثنين: تخطيط «one» (الصورة وحدها، والكلمات على الأرضية الليلية تحتها، وعنوان المكان الذي يبقى صادقاً حتى بلا صورة) مع ارتفاع صورة «scene» وصفّها الشمسي الصغير.</p>
<div class="flow">{phone_html}</div>
<div class="flow" style="grid-template-columns:1fr">{wide_html}</div>
<div class="pair" style="align-items:start"><figure class="new"><img src="{full_a}" alt="" loading="lazy"><figcaption><b>صفحة مصباح الممرّ كاملة</b>المعرض والشراء ← <b>الصورة والعنوان</b> ← <b>כשמחשיך</b> ← الأرقام ← «עוד לאותו מקום» ← الفوتر. {scr(A, "pdp-path-m-js")} شاشة هاتف (السقف 6).</figcaption></figure><figure class="new"><img src="{full_b}" alt="" loading="lazy"><figcaption><b>صفحة الكشّاف كاملة</b>الحالة بلا صورة: النصّ والصفّ الشمسي فقط. {scr(A, "pdp-flood-m-js")} شاشة.</figcaption></figure></div>
<div><h3>القياس على الصفحات الخمس (390×844، بجافاسكربت)</h3>
<div style="overflow-x:auto"><table><thead><tr><th>الصفحة</th><th>قبل</th><th>بعد</th><th>ارتفاع القسمين (بكسل)</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="muted">السقف 6 شاشات لكل صفحة منتج؛ قسم الصورة ≤ 640 بكسل بصورة و≤ 220 بلا صورة؛ الصفّ الشمسي ≤ 160. كل فحوص الجولة السابقة ثابتة على الثلاثين لقطة: نموذج شراء واحد، شريط لاصق واحد، سطر شروط واحد، سطر «תמונה של המקום» واحد، صفر واتساب، صفر أخطاء Liquid، لا فيض أفقي، ورابط دليل واحد بالضبط.</p>
<h3 style="margin-top:34px">من أين جاءت الصور</h3>
<p>لا صورة من خارج المتجر هذه المرة، ولا صورة منتج آخر: فتّشتُ معارض منتجاتك السبعة والعشرين (165 إطاراً) إطاراً إطاراً. خمسة عشر منتجاً عنده إطار ليلي نظيف من معرضه (بلا نصّ مطبوع ولا شارات ولا علامة أجنبية)، أو إطار يصير نظيفاً بقصّ يُخبز في الملف نفسه — وهذه هي الصور على الثيم. الصورة الأولى في المعرض (التي يراها الهاتف) لا تُستعمل أبداً؛ الإطار المختار من داخل المعرض، الذي لا يصل إليه من لا يسحب.</p>
<div class="tablewrap" style="overflow-x:auto"><table><thead><tr><th>المنتج</th><th>الملف على الثيم</th><th>رقم الصورة في معرضه</th><th>القصّ</th></tr></thead><tbody>{src_rows}</tbody></table></div>
<p><b>اثنا عشر منتجاً بلا صورة في هذا القسم</b> لأن كل إطار في معرضها فيه نصّ مطبوع أو شارة أرقام أو علامة أجنبية أو وجوه: {nophoto_html}. عندها القسم يعرض النصّ وحده. الأمر بيدك بثلاث طرق، كلها في محرّر الثيم بلا كود: (1) ترفع إطاراً نظيفاً وتضيف «بلوك» للمنتج في القسم؛ (2) تشغّل خيار «صورة الكولكشن» فيعرض القسم مشهد الكولكشن مع سطر «בתמונה: {{اسم المنتج المصوَّر}}» يربط إليه — مطفأ افتراضياً، لأنك قلت لا صور منتجات مبدَّلة؛ (3) تتركه نصّاً.</p>
<h3 style="margin-top:34px">النصوص، للموافقة</h3>
<p>كل جملة عبرية على القسمين، حرفياً، وكلّها حقول في محرّر الثيم:</p>
<ul class="list">{copy_html}</ul>
<h3 style="margin-top:34px">ما وجده النقد على اللقطات الحقيقية</h3>
{crit_html}
<h3 style="margin-top:34px">ملاحظات لك</h3>
<ul class="list">
<li><b>الصفّ الشمسي يعرف من شمسي ومن لا.</b> الاختبار نفسه الذي يستعمله سطر «לא מתאים»: حقل power_source إن وُجد، وإلا كلمة «סולארי» في العنوان أو الوصف. 16 منتجاً شمسياً و11 لا (مصابيح الجدار الكهربائية، السبوت المغناطيسي، العمود الكهربائي، ثنائي الرأس، فانوس التخييم، الجرلندة بـUSB، الشبكة 220V، أغصان البتولا).</li>
<li><b>الصور الأثقل من 220 كيلوبايت:</b> ثلاث صور (الستانلس، الأعمدة القوية، مشهد الممرّ) بين 287 و304 كيلوبايت لأن الضغط الأقوى كان يفسد الظلال. الهاتف يحمّل نسخة 600 أو 900 بكسل، لا الأصل.</li>
<li><b>صورة الدرج الدافئ</b> (warm-step) مقصوصة إلى 854 بكسل عرضاً — الأنعم على شاشة الحاسوب؛ تستحقّ إطاراً أعرض حين يتوفّر.</li>
<li><b>لم يتغيّر شيء غير ذلك:</b> لا منتج، لا كولكشن، لا صفحة، لا حقل بيانات؛ الثيم الحي كما هو.</li>
</ul>
</div></section>'''
json.dump({'html': html}, open(f'{P}/OWNER-SECTION.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('written', f'{P}/OWNER-SECTION.json', len(html) // 1024, 'KB', '| critique:', 'real' if CRIT else 'placeholder')
