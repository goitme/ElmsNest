#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Owner-page section for the HOME round 2 (Arabic). Writes home2/OWNER-SECTION.json ({"html": ...}) which
simplify/build-owner-page.py splices into the owner page (same Artifact URL). Photographs = the real render of the
dev theme (home2/verify/*.png from shoot-sections.js), embedded as JPEG data URIs. The critique paragraph comes from
home2/critique/SUMMARY.json when it exists (written by the lead after the skeptics), else an honest placeholder."""
import base64, io, json, os
from PIL import Image
H = '/home/user/ElmsNest/brief/side-pages/home2'; V = f'{H}/verify'; SIM = '/home/user/ElmsNest/brief/side-pages/simplify'
CRIT = json.load(open(f'{H}/critique/SUMMARY.json', encoding='utf-8')) if os.path.exists(f'{H}/critique/SUMMARY.json') else None
A = json.load(open(f'{SIM}/verify-after/verify.json'))
def jpg(path, width=390, q=80):
    if not os.path.exists(path): return ''
    im = Image.open(path).convert('RGB')
    if im.width > width: im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
home = A.get('home-m-js', {}); screens = home.get('screens', '—')
hi = {x['section']: x for x in home.get('homeImages', [])}
h = lambda k: hi.get(k, {}).get('h', '—')
phone = [(f'{V}/solar-m.png', 'ביום נטען. בלילה נדלק.', 'نفس نوع المكان نهاراً وليلاً: اللوح يشحن، وعند الغروب يضيء وحده. ثلاث خطوات تحته، بلا زرّ ولا رابط. صورتان من صور منتجك «powerful solar garden light» (الثانية والثالثة في المعرض).'),
         (f'{V}/winter-m.png', 'ובחורף?', 'الملاحظة الصادقة: في الشتاء الشمس أقصر واللوح يشحن أقل — «وهذا صحيح لكل إضاءة شمسية، ومنها إضاءتنا». الصورة: لقطة المساء الماطر من معرض «modern solar path lights set» (السادسة)، مقصوصة بحيث لا يظهر منها نصّ التسويق المطبوع.'),
         (f'{V}/band-m-viewport.png', 'חושך הוא לא סוף הערב.', 'نَفَس بين صفوف «متى نعم ومتى لا» وشريط الأرقام: صورة واحدة بعرض الشاشة وجملة واحدة. الصورة الخامسة من معرض «solar crystal ball string lights».')]
phone_html = ''.join(f'<figure><img src="{jpg(p)}" alt="" loading="lazy"><figcaption><b dir="rtl">{t}</b>{d}</figcaption></figure>' for p, t, d in phone)
wide = [(f'{V}/solar-d.png', 'القسم نفسه على شاشة 1366: الإطاران جنباً إلى جنب (النهار على اليمين، الليل على اليسار) والخطوات الثلاث في صفّ واحد.'),
        (f'{V}/band-d-viewport.png', 'صورة السياج على شاشة 1366، حيث تجلس الجملة على السياج المعتم.')]
wide_html = ''.join(f'<figure class="wide"><img src="{jpg(p, 1140, 74)}" alt="" loading="lazy"><figcaption>{d}</figcaption></figure>' for p, d in wide)
full = jpg(f'{SIM}/verify-after/home-m-js-full.png')
sources = [('ens-home-day.jpg', 'Powerful Solar Garden Light — الصورة 3', 'كاملة', 'أعمدة الحديقة نهاراً، اللوح ظاهر على كل رأس، المصابيح مطفأة.'),
           ('ens-home-night.jpg', 'Powerful Solar Garden Light — الصورة 2', 'الجزء العلوي 1254×1090', 'الأعمدة نفسها ليلاً؛ قُصّ أسفل الصورة لأن فيه سطراً مطبوعاً.'),
           ('ens-home-winter.jpg', 'Modern Solar Path Lights Set — الصورة 6', 'قصّ 150,450 → 1100×580', 'مساء ماطر: ممرّ مبلّل، أعمدتك على العشب، نوافذ مضاءة. عنوان التسويق والشارة خارج القصّ.'),
           ('ens-home-fence.jpg', 'Solar Crystal Ball String Lights — الصورة 5', 'كاملة', 'كرات كريستال على سياج خشبي في الساعة الزرقاء، جهنمية، أضواء المدينة خلفه.')]
src_rows = ''.join(f'<tr><td dir="ltr" style="font-family:ui-monospace,monospace;font-size:13px">{a}</td><td>{s}</td><td>{c}</td><td>{w}</td></tr>' for a, s, c, w in sources)
copy = [('תאורה סולארית', 'سطر افتتاحي صغير: يحصر الحقائق الثلاث في المنتجات الشمسية (مصباح الجدار الكهربائي في البطاقات فوقه ليس شمسياً).'),
        ('יום · לילה', 'تسميتا الزاويتين.'), ('ביום נטען. · בלילה נדלק.', 'العنوان مقسوماً على الإطارين.'),
        ('הפאנל נטען לאור היום. · כשמחשיך, האור נדלק לבד. · בלי כבל, בלי חשמלאי.', 'الخطوات الثلاث — كما تقول نقاط منتجاتك نفسها («הפעלה אוטומטית בחושך»).'),
        ('ובחורף?', 'عنوان قسم الشتاء.'),
        ('בחורף השמש קצרה יותר, והפאנל נטען פחות. · פחות טעינה ביום, פחות אור בלילה. · זה נכון לכל תאורה סולארית, גם שלנו.', 'ثلاثة أسطر؛ الثالث هو صدق العلامة معلناً — طلبه الحكّام الخمسة.'),
        ('חושך הוא לא סוף הערב.', 'جملة واحدة على صورة السياج. ليست ادّعاءً.')]
copy_html = ''.join(f'<li><b dir="rtl" lang="he">{he}</b><span class="muted"> — {ar}</span></li>' for he, ar in copy)
crit_html = CRIT['html'] if CRIT else '<p class="muted">النقد العدائي على اللقطات الحقيقية يعمل الآن (خمس عدسات: مشترٍ، أنت، حارس الصدق، مصمّم، مهندس؛ ومشكّكان على كل ملاحظة). نتيجته تُضاف هنا عند اكتماله.</p>'
html = f'''<section id="home2"><div class="wrap">
<p class="eyebrow">الرئيسية · الجولة الثانية</p><h2>ثلاثة أقسام بالصور على الرئيسية</h2>
<blockquote>«اريد منك ان تزيد محتوى لكن لا تزيد كثير زيد يعني 2-3 سكشنز و اهم شيء ان اتصنع السكشن مع صور يعني ابحث عن صور مناسبة للنيش و قوم بوضعها في السكشن بشكل ابداعي جميل»<small>طلبك، 2026-09-06</small></blockquote>
<p>ثلاثة أقسام، لا أكثر، بين بطاقات المنتجات وشريط الأرقام: <b>نهار/ليل</b> بثلاث خطوات، <b>وفي الشتاء؟</b> بصورة واحدة وثلاثة أسطر، و<b>نَفَس</b> بصورة واحدة وجملة واحدة. الصور الأربع كلها من معارض منتجاتك أنت (الصور الثانوية لثلاث قوائم)، فلا صورة على الصفحة تدّعي أنها غير منتجاتك، ولا حقّ نشر لأحد. الصفحة على هاتف 390×844: <b>{screens}</b> شاشة (كانت 5.12، والسقف 7.5)؛ الأقسام الثلاثة {h('ens-home-solar')} / {h('ens-home-winter')} / {h('ens-home-band')} بكسل (السقف 520 لكلّ منها). لا جافاسكربت جديدة، لا أزرار، لا روابط؛ كل نصّ وكل صورة قابلان للتغيير من محرّر الثيم.</p>
<div class="flow">{phone_html}</div>
<div class="flow" style="grid-template-columns:1fr">{wide_html}</div>
<div class="pair" style="grid-template-columns:minmax(0,300px) 1fr;align-items:start"><figure class="new"><img src="{full}" alt="" loading="lazy"><figcaption><b>الرئيسية كاملة على هاتف</b>الترتيب: البطل، الكولكشنات الأربع، أربعة منتجات، <span dir="rtl">نهار/ليل</span>، الشتاء، «متى نعم ومتى لا»، صورة السياج، الأرقام الثلاثة، الفوتر.</figcaption></figure>
<div><h3>من أين جاءت الصور</h3><p>بحثتُ أولاً خارج المتجر: 498 صورة مرشّحة من Openverse وWikimedia Commons برخص حرّة (CC0 وملك عام وCC BY)، قُيّمت واحدةً واحدة على ورقة اتصال. ثم قارنتها بالصور الثانوية في معارض منتجاتك، فتبيّن أن أفضل صور «حياة» للحديقة ليلاً هي عندك أصلاً — فاستُعملت هي وحدها. لم يُشترَ ولم يُولَّد شيء (رصيد التوليد لم يُمسّ). خمسة مفاهيم رُسمت بالصور الحقيقية وحكم عليها خمسة حكّام؛ فاز مفهوم «إطاران» بالإجماع، وأُخذت منه شاشتان، ومن مفهوم «النَفَس» شاشته الوحيدة الأفضل.</p>
<div class="tablewrap" style="overflow-x:auto"><table><thead><tr><th>الملف على الثيم</th><th>المصدر (معرض منتجك)</th><th>القصّ</th><th>ما في الصورة</th></tr></thead><tbody>{src_rows}</tbody></table></div></div></div>
<h3 style="margin-top:34px">النصوص، للموافقة</h3>
<p>كل جملة عبرية على الأقسام الثلاثة، حرفياً. لا أرقام، لا مراتب، لا استعجال، لا تقييمات:</p>
<ul class="list">{copy_html}</ul>
<h3 style="margin-top:34px">ما وجده النقد على اللقطات الحقيقية</h3>
{crit_html}
<h3 style="margin-top:34px">ملاحظات لك</h3>
<ul class="list">
<li><b>صور المنتجات كديكور للرئيسية.</b> الصورة الثانية والثالثة من «powerful solar garden light» والسادسة من «modern solar path lights set» والخامسة من «crystal ball» تظهر الآن على الرئيسية بلا اسم المنتج. إن أردت غير ذلك، لكل قسم حقل صورة في محرّر الثيم يستبدلها بأي صورة تختارها (وحقل «موضع القصّ» يحرّكها).</li>
<li><b>وزن الصور.</b> الملفات الأصلية على الثيم بين 165 و294 كيلوبايت (أعلى من سقف 220 الذي وضعتُه لنفسي، لأن صورة النهار كانت تفقد تفاصيلها تحته)؛ الهاتف لا يحمّل الأصل بل نسخة 600 أو 900 بكسل من CDN Shopify، والصور كلها مؤجّلة التحميل حتى يصل إليها التمرير.</li>
<li><b>ملف اختبار صغير</b> باسم <span dir="ltr">assets/ens-test.png</span> (75 بايت) بقي على ثيم التطوير من تجربة مسار الرفع؛ أداة الحذف ممنوعة عليّ، فاحذفه من محرّر الكود إن شئت. لا شيء يشير إليه.</li>
<li><b>لم يتغيّر شيء غير ذلك:</b> لا منتج، لا كولكشن، لا صفحة، لا حقل بيانات؛ الثيم الحي كما هو.</li>
</ul>
</div></section>'''
json.dump({'html': html}, open(f'{H}/OWNER-SECTION.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('written', f'{H}/OWNER-SECTION.json', len(html) // 1024, 'KB', '| critique:', 'real' if CRIT else 'placeholder')
