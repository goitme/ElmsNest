#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""From the critique workflow's return (saved verbatim as critique/RESULT.json by the lead) write one jsonl per lens
(critique/<lens>.jsonl: the findings with both skeptics' votes) and critique/SUMMARY.json ({"html": ...}, Arabic) for
the owner page. The rulings are in LEAD-DECISIONS.md and are not derived from the votes: the votes are the record."""
import json, os
H = '/home/user/ElmsNest/brief/side-pages/home2/critique'
R = json.load(open(f'{H}/RESULT.json', encoding='utf-8'))
by = {}
for f in R['findings']: by.setdefault(f['lens'], []).append(f)
for lens, fs in by.items():
    with open(f'{H}/{lens}.jsonl', 'w', encoding='utf-8') as out:
        for f in fs: out.write(json.dumps(f, ensure_ascii=False) + '\n')
import re
STALE = re.compile(r'already (does|has|do|carr|exist|uses|is|reads|ends|decided|applied)|stale|no longer|superseded|pre-fix|pre-critique|pre-amendment|before the fix|the file as it stands|does not exist in the file|describes (markup|code|a pass-1|the committed|the first build)|not on the rendered page|first build', re.I)
def kind(f):
    vs = f.get('votes', [])
    if not vs: return 'unvoted'
    if all(not v['refuted'] for v in vs): return 'confirmed'
    # a "refuted" vote whose reason says the file already does what the fix asks = the lead had fixed it before the skeptic looked
    if any(v['refuted'] and STALE.search(v['reason'] or '') for v in vs): return 'fixed-before-vote'
    if all(v['refuted'] for v in vs): return 'refuted'
    return 'split'
kinds = {}
for f in R['findings']: f['kind'] = kind(f); kinds[f['kind']] = kinds.get(f['kind'], 0) + 1
n = len(R['findings']); surv = sum(1 for f in R['findings'] if f.get('survives'))
both = kinds.get('confirmed', 0); refuted = kinds.get('refuted', 0); fixed = kinds.get('fixed-before-vote', 0); split = kinds.get('split', 0)
scores = ' · '.join(f"{ {'shopper':'المشتري','owner':'أنت','honesty':'حارس الصدق','designer':'المصمّم','engineer':'المهندس'}.get(l['lens'], l['lens'])} {l['score']}" for l in R['lenses'])
html = f'''
<p>خمس عدسات قرأت اللقطات الحقيقية للأقسام الثلاثة على ثيم التطوير (360 و390 و1366): مشترٍ لأول مرة على هاتف، أنت بحكمك «بسيط، لا شيء مرتين، صورك أنت»، حارس الصدق على النصوص والصور، مصمّم على الحرفة، ومهندس على الشيفرة. الدرجات من عشرة: {scores}. <b>{n} ملاحظة</b>، وعلى كل واحدة مشكّكان مستقلان (أحدهما يفحص الدليل في اللقطات والأرقام، والآخر يفحص إن كان التغيير صائباً بحسب العقد وحكمك). أحكامي كُتبت قبل أن يُنفَّذ أي إصلاح (<span dir="ltr">critique/LEAD-DECISIONS.md</span>)، لكن المشكّكين عملوا ببطء بينما كانت الإصلاحات تُنشر — فكثير من «النقض» عندهم يعني «الملف يفعل ذلك أصلاً». بالعدّ الصادق: {both} أكّدها الاثنان، {fixed} وجدها المشكّك مُصلَحة قبل أن ينظر، {refuted} نُقضت على أساسها (وقد نُفّذ بعضها مع ذلك لأن حكمك «لا شيء مرتين» يعلو على نصّ العقد)، و{split} انقسمت. ثم نُشرت الإصلاحات وقِيست من جديد، وراجعها مراجعان آخران (عقد وعرض) مع مشكّك على كل ملاحظة: أربع ملاحظات صغيرة، ثلاث نُفّذت (تصحيح حرفي في نصّ بديل، ورفع قصّ صورتين على الحاسوب حتى لا تُقطع نورة أو رأس مصباح عند الحافة) وواحدة قُبلت كما هي.</p>
<h4 style="margin:18px 0 6px">ما تغيّر بعد النقد</h4>
<ul class="list">
<li><b>كلمتا الزاوية «יום»/«לילה» أُطفئتا.</b> قِيست كلمة «יום» فوق أوراق الشجر المضيئة عند 1.2–1.8 إلى 1 (الحدّ 4.5) في الأحجام الثلاثة؛ والعنوانان على الإطارين يقولان نهاراً وليلاً أصلاً — «لا شيء مرتين». بقي الحقلان في المحرّر فارغين، وإن كتبتَ كلمة فستجلس على خلفية ليلية تجعلها مقروءة على أي صورة (قِيست 14 إلى 1).</li>
<li><b>ثلاث خطوات مرقّمة صارت سطراً واحداً.</b> «ביום נטען.» كانت هي الخطوة 1، و«בלילה נדלק.» مع جملة البطل «כשהשמש יורדת, הגינה נדלקת.» هما الخطوة 2. بقي ما هو جديد: «בלי חיבור לחשמל, בלי חשמלאי.» — وهي عبارة قوائم منتجاتك (كانت «בלי כבל» وهي غير دقيقة للكشّاف ذي اللوح المنفصل).</li>
<li><b>سطر الافتتاح الصغير صار عنواناً.</b> «תאורה סולארית» بحرف 13 لم تكن كافية لحصر الحقائق في المنتجات الشمسية (مصباح الجدار الكهربائي في البطاقات فوقها). صارت «איך עובדת תאורה סולארית?» بحجم عناوين الأقسام المجاورة، وسؤالها يقود إلى «ובחורף?» بعدها.</li>
<li><b>جملة السياج على الحاسوب.</b> عند 1366 كانت المحرزة السفلية من كرات الكريستال تمرّ خلف الجملة (3.5 إلى 1). قِيست ثلاثة حلول: رفع القصّ (6.6 إلى 1، الصورة نظيفة) فاز على تعميق التدرّج (4.6 إلى 1 وتعكير الإطار). الافتراضي صار «50% 40%» ويبقى حقلاً في المحرّر.</li>
<li><b>أصغر:</b> إطار الشتاء فقد حدّه الرفيع (لا صورة على الصفحة لها إطار)؛ عنوانه بحجم جيرانه؛ قصّ النهار والليل على الحاسوب يُظهر اللوح كاملاً ورؤوس المصابيح البعيدة؛ تعتيم إطار الليل أعمق قليلاً (6.4 إلى 1 خلف العنوان الذهبي عند 360)؛ صورة السياج في التدفّق لا فوقه؛ حُذف بديل 1200 بكسل من قوائم الصور لأن إعادة ترميزه في CDN أثقل من الأصل (347 ضد 249 كيلوبايت) وهو ما كان الهاتف يختاره؛ حقل «نصّ بديل» لكل صورة؛ لا اسم مختلَق للقسم إن أُفرغت جملته.</li>
</ul>
<h4 style="margin:18px 0 6px">ما لم أغيّره، وهو لك</h4>
<ul class="list">
<li><b>بطاقة المنتج الثانية هي منتج الإطارين.</b> عدسة «المالك» رأت أن «powerful solar garden light» يظهر بطاقةً في «מה שנדלק ראשון» ثم إطارين نهاراً وليلاً تحتها بأربعمئة بكسل، وطلبت استبدال البطاقة بمنتج آخر. رأيي: صورة المنتج ثم المنتج في مكانه هو زوج عادي في المتاجر لا تكراراً لحقيقة؛ وقائمة المنتجات الأربعة قرارك من جولة التبسيط. إن أردت الاستبدال فهو سطر واحد في القالب (<span dir="ltr">product_list</span>).</li>
<li><b>جملة السياج وجملة البطل.</b> العدسة نفسها رأتهما فكرة واحدة («عندما تغيب الشمس تضيء الحديقة» / «الظلام ليس نهاية المساء»). أبقيتُ الجملة لأن الأولى عن المصابيح والثانية عن الناس. حقل واحد إن أردت غيرها.</li>
<li><b>مشهد رابع بالأعمدة.</b> صورة الشتاء عمودٌ رابع على الصفحة (البطل، بلاطة الممرّ، البطاقة، الإطاران). لا صورة في معارضك بمطر أو غسق شتوي لمنتج جدار أو كشّاف؛ الحقل في المحرّر يبدّلها بنقرة.</li>
<li><b>رابط على صورة السياج.</b> اقترح المشتري حقل رابط اختيارياً يقود إلى كولكشن الغرلاندات؛ لم أضفه (المواصفة: بلا رابط ولا زرّ). عشرة أسطر إن أردته.</li>
</ul>
'''
json.dump({'html': html, 'n': n, 'survives': surv, 'confirmed': both, 'fixed_before_vote': fixed, 'refuted': refuted, 'split': split}, open(f'{H}/SUMMARY.json', 'w', encoding='utf-8'), ensure_ascii=False)
print(f'{n} findings: {both} confirmed by both, {fixed} already fixed when the skeptic looked, {refuted} refuted on the merits, {split} split → SUMMARY.json + {len(by)} jsonl files')
