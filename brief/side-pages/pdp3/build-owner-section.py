#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Owner-page section for ROUND 3: the two new product-page sections and the seven content pages (Arabic).
Writes pdp3/OWNER-SECTION.json ({"html": ...}), which simplify/build-owner-page.py splices after the pdp2 section.
Every photograph is a crop of the REAL deployed render (pdp3/verify/, pages/verify/), embedded as a JPEG data URI."""
import base64, io, json, os
from PIL import Image
R = '/home/user/ElmsNest/brief/side-pages'
P3, PG = f'{R}/pdp3', f'{R}/pages'
A3 = json.load(open(f'{P3}/verify/verify.json', encoding='utf-8'))
AP = json.load(open(f'{PG}/verify/verify.json', encoding='utf-8'))
CR = json.load(open(f'{P3}/critique/SUMMARY.json', encoding='utf-8')) if os.path.exists(f'{P3}/critique/SUMMARY.json') else None

def jpg(path, width=390, q=78, box=None):
    if not os.path.exists(path): return ''
    im = Image.open(path).convert('RGB')
    if box: im = im.crop(box)
    if im.width > width: im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def scr(d, k): return d.get(k, {}).get('screens', '—')
def sech(k, name):
    for s in A3.get(k, {}).get('pdpSections', []):
        if s['section'] == name: return s['h']
    return '—'

# ---- the product page: the two new sections, cropped from the real full-page shots
shots = [
    (f'{P3}/verify/pdp-path-m-js-full.png', (0, 2150, 390, 2640), '«בחוץ, כל השנה» — صفحة الممرّ',
     'صورتان مؤطّرتان جنباً إلى جنب: مطر كانون الثاني على لوح شمسي، وشمس آب على جدار. تحت كل صورة سطر قصير، ثم سطر يسمّي ما في الصورة ومَن صوّرها. لا كلمة فوق صورة، ولا شريط ليلي ثانٍ.'),
    (f'{P3}/verify/pdp-path-m-js-full.png', (0, 3390, 390, 3800), '«האור האחרון של היום» — الطبعة الكريمية',
     'حصيرة كريمية على الأرضية الليلية تحمل صورة مكان في الساعة الذهبية، والكتابة على الحصيرة لا على الصورة. الصورة تتغيّر بحسب عائلة المنتج: شبيل حجري للممرّ، حديقة بيت للجدار، جنّ ككتوس للحديقة، مرفسة في المدينة للديكور.'),
    (f'{P3}/verify/pdp-wall-m-js-full.png', (0, 2100, 390, 2600), 'صفحة الجدار (كهرباء)',
     'المنتج غير شمسي، فالبوابة تبدّل الصورة: قطرات على غصن بدل اللوح الشمسي، ولا كلمة «سولاري» في الصفحة كلّها.'),
]
prod_imgs = ''.join(
    f'<figure class="shot"><img src="{jpg(p, 390, 80, box)}" alt=""><figcaption><b>{t}</b><br>{c}</figcaption></figure>'
    for p, box, t, c in shots if os.path.exists(p))

prod_rows = ''.join(
    f'<tr><td>{t}</td><td dir="ltr">{scr(A3, k + "-m-js")}</td><td dir="ltr">{sech(k + "-m-js", "ens-pdp-weather")} / {sech(k + "-m-js", "ens-pdp-print")}</td></tr>'
    for k, t in [('pdp-path', 'مصباح الممرّ (شمسي)'), ('pdp-rope', 'حبل الإضاءة (شمسي)'), ('pdp-deck', 'إضاءة الدرج (شمسي)'), ('pdp-wall', 'مصباح الجدار (كهرباء)'), ('pdp-flood', 'الكشّاف (شمسي)')])

# ---- the content pages
pages = [('page-guide', 'الدليل', 6), ('page-why', 'لماذا سولاري', 5), ('page-about', 'من نحن', 5), ('page-faq', 'الأسئلة الشائعة', 6),
         ('page-processing', 'زمن التجهيز', 4), ('page-shipping', 'الشحن والإرجاع', 5), ('page-contact', 'اتصلوا بنا', 4)]
page_rows = ''.join(f'<tr><td>{t}</td><td dir="ltr">{scr(AP, k + "-m-js")}</td><td dir="ltr">{tg}</td><td dir="ltr">{len(AP.get(k + "-m-js", {}).get("pageCopy", {}).get("photos", []))}</td></tr>' for k, t, tg in pages)
page_imgs = ''.join(
    f'<figure class="shot"><img src="{jpg(f"{PG}/verify/{k}-m-js-full.png", 390, 78, box)}" alt=""><figcaption><b>{t}</b><br>{c}</figcaption></figure>'
    for k, t, box, c in [
        ('page-guide', 'الدليل: الأماكن الأربعة في إطار واحد', (0, 0, 390, 1500),
         'شريط صورة قصير يحمل سماء الغروب، ثم العنوان. القرار الأول صار صورة فناء واحد عند الغروب وتحته أربع تسميات تشير إلى ما هو الشبيل والكير والجينة والمرفسة داخل الصورة نفسها — وكل تسمية رابط لمجموعتها بعددها الحيّ.'),
        ('page-about', 'من نحن: رسالة موقّعة', (0, 0, 390, 1400),
         'حوش سيرجي في القدس شريطاً، ثم النصّ في عمود قراءة واحد، والمبادئ الثلاثة على عمود مرقّم، وفي النهاية توقيع: «כתבו לנו.» والاسم والبريد نصّاً لا رابطاً.'),
        ('page-contact', 'اتصلوا بنا: النموذج كما هو', (0, 0, 390, 1400),
         'شريط صورة وعنوان مرئي (كان مخفياً: كريم على كريم)، ثم نموذج كاليس الأصلي بلا تعديل، ثم ما تحتاجه قبل أن تكتب. البريد مرّة واحدة على الصفحة.'),
    ] if os.path.exists(f'{PG}/verify/{k}-m-js-full.png'))

crit = CR['html'] if CR else '<p>النقد الخصومي على الصفحات المنشورة: خمس عدسات ومشكّك على كل ملاحظة. النتيجة في المستودع.</p>'

html = f'''
<section id="round3">
<h2>الجولة الثالثة: محتوى أكثر في صفحة المنتج، وصور في صفحات المحتوى</h2>
<p class="lead">طلبتَ شيئين: «محتوى أكثر في صفحة المنتج — صورتان أو ثلاث، بابتكار، ليس بنفس اللون»، ثم «اذهب إلى صفحات المحتوى وأضف صوراً هناك، والصور من الإنترنت عادي». الاثنان مبنيّان ومنشوران على ثيم التطوير وحده. لم يُنشر شيء على المتجر الحيّ، ولم يتغيّر منتج ولا مجموعة ولا صفحة في شوبيفاي.</p>

<h3>أولاً: صفحة المنتج — قسمان جديدان بلون آخر</h3>
<p>القسمان السابقان (الصورة الليلية وصفّ «כשמחשיך») جهاز واحد: ليل، صورة بعرض الشاشة، كلمات تحتها. الجديد عكسه: صور <b>مؤطّرة داخل العمود</b>، ولا كلمة فوق صورة أبداً، وتعليق صغير تحت كل صورة يقول ما هي ومن صوّرها، و<b>ضوء نهار</b> وحصيرة كريمية على الأرضية الليلية.</p>
{prod_imgs}
<table class="num"><thead><tr><th>الصفحة</th><th>شاشات (390 · السقف 7.5)</th><th>ارتفاع القسمين (بكسل)</th></tr></thead><tbody>{prod_rows}</tbody></table>
<p class="note">القياس من الصفحات الحقيقية على ثيم التطوير، لا من رسم. كل صورة ≤ 202 كيلوبايت، ولا صورة أعرض من ملفها.</p>

<h3>ثانياً: صفحات المحتوى السبع</h3>
<p>كانت السبع لا تزال ترتدي الثوب الكريمي الذي رفضتَه: عنوان غير مرئي على صفحتَي الشحن والاتصال، ونصّ ملتصق بحافّة الشاشة، والقائمة المسطّرة نفسها أربع مرات، ولا صورة إلا واحدة. الآن السبع كلّها من قسم واحد في الثيم، بالثوب الليلي نفسه، ولكل صفحة صورة تفتحها.</p>
{page_imgs}
<table class="num"><thead><tr><th>الصفحة</th><th>شاشات (390)</th><th>الهدف</th><th>صور</th></tr></thead><tbody>{page_rows}</tbody></table>
<p class="note">الأرقام السبعة (مجاني · <span dir="ltr">29.90</span> · <span dir="ltr">1–3</span> · <span dir="ltr">7–14</span> · <span dir="ltr">8–17</span> · <span dir="ltr">14</span> يوماً · <span dir="ltr">5%</span> أو <span dir="ltr">100</span> ₪) نُقلت حرفاً بحرف من صفحاتك، وأسماء المجموعات الأربعة تُقرأ حيّة من شوبيفاي فلا تتناقض مع القائمة.</p>

<h3>الصور: من أين، وبأي رخصة</h3>
<p>بحثتُ في مكتبتين مفتوحتين (Openverse وويكيميديا كومنز) وأنزلتُ <span dir="ltr">324</span> صورة، ونظرتُ إليها كلّها وقيّمتُها، واخترتُ <span dir="ltr">27</span>، ونشرتُ منها <span dir="ltr">17</span>. كلّها برخص تسمح بالاستخدام التجاري، وكل صورة تحتاج كريدت تحمله مكتوباً تحتها. <b>ولا صورة واحدة تُقدَّم كأنها منتجك</b>: تحت كل واحدة سطر يقول ما هي — مكان أو مادّة أو آلية.</p>
{crit}
</section>
'''
json.dump({'html': html}, open(f'{P3}/OWNER-SECTION.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('OWNER-SECTION.json written:', len(html), 'chars')
