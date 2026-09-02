#!/bin/bash
# Mirror every side-page template of the dev theme (154726400174) for the inventory.
# Usage: bash brief/inventory/mirror-all.sh   → brief/inventory/<key>/index.html
set -u
cd /home/user/ElmsNest
T=154726400174
OUT=brief/inventory
enc(){ python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1],safe='/'))" "$1"; }
declare -A P
P[coll-all]="/collections/all"
P[coll-wall]="/collections/solar-wall-lights"
P[coll-path]="/collections/$(enc 'תאורת-שביל-סולארית')"
P[coll-decor]="/collections/$(enc 'גרילנדות-ותאורה-דקורטיבית')"
P[coll-spot]="/collections/$(enc 'ספוטים-ופרוז-קטורים-סולאריים')"
P[coll-sale]="/collections/sale"
P[coll-list]="/collections"
P[coll-all-sorted]="/collections/all?sort_by=price-ascending"
P[pdp-single]="/products/stainless-steel-solar-path-light-ip65"
P[pdp-multi]="/products/solar-crystal-ball-string-lights"
P[pdp-wall]="/products/waterproof-led-wall-light-ip65-6w-12w"
P[cart-empty]="/cart"
P[search-hits]="/search?q=$(enc 'שביל')&type=product"
P[search-none]="/search?q=zzqqxx"
P[search-blank]="/search"
P[p404]="/this-page-does-not-exist-404"
P[page-guide]="/pages/guide-garden-lighting"
P[page-why-solar]="/pages/why-solar-lighting"
P[page-about]="/pages/$(enc 'מי-אנחנו')"
P[page-shipping]="/pages/shipping-delivery"
P[page-faq]="/pages/help-faq"
P[page-contact]="/pages/contact-us"
P[page-processing]="/pages/processing-time"
P[page-accessibility]="/pages/accessibility-statement"
P[policy-refund]="/policies/refund-policy"
P[policy-shipping]="/policies/shipping-policy"
P[policy-terms]="/policies/terms-of-service"
P[policy-privacy]="/policies/privacy-policy"
P[account-login]="/account/login"
P[account-register]="/account/register"
P[blog-news]="/blogs/news"
P[home]="/"
run(){
  k=$1; path=$2
  if [[ "$path" == *\?* ]]; then url="https://elmsnest.com${path}&preview_theme_id=$T"; else url="https://elmsnest.com${path}?preview_theme_id=$T"; fi
  mkdir -p "$OUT/$k"
  python3 brief/mirror.py "$url" "$OUT/$k" > "$OUT/$k/mirror.log" 2>&1
  echo "$k: $(tail -1 $OUT/$k/mirror.log)"
}
export -f run enc; export T OUT
for k in "${!P[@]}"; do echo "$k ${P[$k]}"; done | xargs -P 4 -L 1 bash -c 'run "$0" "$1"'
# cart with items: add two lines to a fresh jar, then mirror /cart with that jar
k=cart-full; mkdir -p $OUT/$k; CJ=$OUT/$k/cj.txt; rm -f $CJ
curl -sSL -c $CJ -b $CJ -o /dev/null "https://elmsnest.com/?preview_theme_id=$T"
V1=$(curl -sSL -b $CJ "https://elmsnest.com/products/stainless-steel-solar-path-light-ip65.js" | python3 -c "import json,sys;print(json.load(sys.stdin)['variants'][0]['id'])")
V2=$(curl -sSL -b $CJ "https://elmsnest.com/products/solar-crystal-ball-string-lights.js" | python3 -c "import json,sys;print(json.load(sys.stdin)['variants'][2]['id'])")
curl -sS -c $CJ -b $CJ -o /dev/null -w "add1 %{http_code}\n" -X POST "https://elmsnest.com/cart/add.js" -H 'Content-Type: application/json' -d "{\"id\":$V1,\"quantity\":2}"
curl -sS -c $CJ -b $CJ -o /dev/null -w "add2 %{http_code}\n" -X POST "https://elmsnest.com/cart/add.js" -H 'Content-Type: application/json' -d "{\"id\":$V2,\"quantity\":1}"
python3 brief/mirror.py "https://elmsnest.com/cart?preview_theme_id=$T" "$OUT/$k" > "$OUT/$k/mirror.log" 2>&1; echo "$k: $(tail -1 $OUT/$k/mirror.log)"
echo ALL-MIRRORED
