
    (function() {
      var preconnectOrigins = ["https://cdn.shopify.com"];
      var scripts = ["/cdn/shopifycloud/checkout-web/assets/c1/polyfills-legacy.uV-pN8XV.js","/cdn/shopifycloud/checkout-web/assets/c1/app-legacy.CA6sSEqC.js","/cdn/shopifycloud/checkout-web/assets/c1/esnext-vendor-legacy.jYLyUHgV.js","/cdn/shopifycloud/checkout-web/assets/c1/context-browser-legacy.qgABAzAe.js","/cdn/shopifycloud/checkout-web/assets/c1/checkout-policy-legacy.BEmlktit.js","/cdn/shopifycloud/checkout-web/assets/c1/helpers-setAddressErrors-legacy.DrDGqdbS.js","/cdn/shopifycloud/checkout-web/assets/c1/types-ShopPayInstallments-legacy.Dv1qjkJY.js","/cdn/shopifycloud/checkout-web/assets/c1/receipt-mapper-load-recovery-legacy.W6CSirHU.js","/cdn/shopifycloud/checkout-web/assets/c1/receipt-eager-mappers-legacy.C48okccN.js","/cdn/shopifycloud/checkout-web/assets/c1/consent-manager-shared-legacy.CtkiS5D-.js","/cdn/shopifycloud/checkout-web/assets/c1/sections-shared-legacy.BvCHcPi1.js","/cdn/shopifycloud/checkout-web/assets/c1/error-logger-report-graphql-error-legacy.BVZkRsWT.js","/cdn/shopifycloud/checkout-web/assets/c1/shop-pay-normalizeBuyerDetails-legacy.0SwsP3lQ.js","/cdn/shopifycloud/checkout-web/assets/c1/helpers-derivations-legacy.DRC0MnCy.js","/cdn/shopifycloud/checkout-web/assets/c1/cvv-cvvBridge-legacy.C_HqsjIP.js","/cdn/shopifycloud/checkout-web/assets/c1/PayButton-helpers-legacy.Due_WF_M.js","/cdn/shopifycloud/checkout-web/assets/c1/graphql-redeemable-legacy.CwRUCRsj.js","/cdn/shopifycloud/checkout-web/assets/c1/hydrate-legacy.DdGDHAdw.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useShopPayExternalAppContext-legacy.OFl7q8Ad.js","/cdn/shopifycloud/checkout-web/assets/c1/locale-he-legacy.kVc5-7Sf.js","/cdn/shopifycloud/checkout-web/assets/c1/OnePage-legacy.f03CjvOH.js","/cdn/shopifycloud/checkout-web/assets/c1/components-DeliveryTransition-legacy.DY6p1HS0.js","/cdn/shopifycloud/checkout-web/assets/c1/useShopPayButtonClassName-legacy.Dtqg_Xde.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useSuppressShopPayModalOnLoad-legacy.CBUwDSN-.js","/cdn/shopifycloud/checkout-web/assets/c1/crypto-constants-legacy.amaCtqvI.js","/cdn/shopifycloud/checkout-web/assets/c1/ChangeCompanyLocationLink-legacy.2rgWFaLy.js","/cdn/shopifycloud/checkout-web/assets/c1/BillingAddressForm-legacy.Bo2dQ19D.js","/cdn/shopifycloud/checkout-web/assets/c1/PhoneField-legacy.CT0TJnim.js","/cdn/shopifycloud/checkout-web/assets/c1/ShippingMethodRateLabel-legacy.DXYQkOZX.js","/cdn/shopifycloud/checkout-web/assets/c1/components-RedirectionNotice.module-legacy.B_87EBC5.js","/cdn/shopifycloud/checkout-web/assets/c1/Choice-legacy.hAkcn3Lg.js","/cdn/shopifycloud/checkout-web/assets/c1/Checkbox-legacy.CHllSSEN.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useCanChangeCompanyLocation-legacy.s2sHA7yB.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useUnauthenticatedErrorModal-legacy.DOGwnpWS.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useForceShopPayUrl-legacy.D1azTzAR.js","/cdn/shopifycloud/checkout-web/assets/c1/utilities-previous-legacy.BgOTI-4m.js","/cdn/shopifycloud/checkout-web/assets/c1/ShopPayLogo-legacy.CUThktdu.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useWalletsTimeout-legacy.lWdPal5R.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-usePostPurchase-legacy.BHM8NImc.js","/cdn/shopifycloud/checkout-web/assets/c1/Monorail-monorailMetric-wallets-legacy.Iy87EwWM.js","/cdn/shopifycloud/checkout-web/assets/c1/shop-pay-installments-monorail-legacy.CuVwiuAe.js","/cdn/shopifycloud/checkout-web/assets/c1/IncentiveBadge-legacy.BH_8hyxa.js","/cdn/shopifycloud/checkout-web/assets/c1/AutocompleteField-hooks-legacy.0pZ3ZhgJ.js","/cdn/shopifycloud/checkout-web/assets/c1/PendingShipping-legacy.C5zghK0Z.js","/cdn/shopifycloud/checkout-web/assets/c1/useAddressMutationsWithNegotiation-legacy.CzIWQrzs.js","/cdn/shopifycloud/checkout-web/assets/c1/PaymentIcon-legacy.BeAFfl8u.js","/cdn/shopifycloud/checkout-web/assets/c1/PaymentLine-legacy.CcxHNg5X.js","/cdn/shopifycloud/checkout-web/assets/c1/Theme-ThemeOverride-legacy.DKXWpsTp.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useUpdateCheckoutAddress-legacy.DUIb8WRH.js","/cdn/shopifycloud/checkout-web/assets/c1/payment-usePaymentExemptionReason-legacy.DXTa1DmZ.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useShopPayProgressIntercepts-legacy.DibvqvgO.js","/cdn/shopifycloud/checkout-web/assets/c1/Section-legacy.B5KWw85Z.js","/cdn/shopifycloud/checkout-web/assets/c1/Section-SectionStyleOverride-legacy.Bcu8imvx.js","/cdn/shopifycloud/checkout-web/assets/c1/PaymentErrorBanner-legacy.D-cAW_XN.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useGeneralPaymentErrorMessage-legacy.BR68No2v.js","/cdn/shopifycloud/checkout-web/assets/c1/StickyPayButton-StickyPayButton.module-legacy.BiDhX-g8.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-payment-button-legacy.DIRBM3-J.js","/cdn/shopifycloud/checkout-web/assets/c1/CaptureEvents-ButtonWithRegisterWebPixel-legacy.CyqvJ6jM.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useShouldRevealExtension-legacy.DfLm4GFp.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-usePreselectSpi-legacy.CjBIhBum.js","/cdn/shopifycloud/checkout-web/assets/c1/Switch-legacy.CjFLuIVI.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useAvailableShopPromotionDiscounts-legacy.DmfVqHAG.js","/cdn/shopifycloud/checkout-web/assets/c1/checkout-as-guest-amazon-pay-legacy.DLoFBwr3.js","/cdn/shopifycloud/checkout-web/assets/c1/Middot-legacy.DGATD7NF.js","/cdn/shopifycloud/checkout-web/assets/c1/EstimatedDeliveryContent-legacy.spe1XfYd.js","/cdn/shopifycloud/checkout-web/assets/c1/shipping-methods-consolidated-included-legacy.Coy57Y5t.js","/cdn/shopifycloud/checkout-web/assets/c1/ShippingLines-legacy.6NQKFzh_.js","/cdn/shopifycloud/checkout-web/assets/c1/ShipmentBreakdown-legacy.CNI_Jia2.js","/cdn/shopifycloud/checkout-web/assets/c1/MerchandiseModal-legacy.B2_GOR9E.js","/cdn/shopifycloud/checkout-web/assets/c1/ShippingMethodSelector-legacy.dIiu-3yt.js","/cdn/shopifycloud/checkout-web/assets/c1/TextArea-legacy.U-wZAmzG.js","/cdn/shopifycloud/checkout-web/assets/c1/SubscriptionPriceBreakdown-legacy.oYTk668J.js","/cdn/shopifycloud/checkout-web/assets/c1/StockProblems-StockProblemsLineItemList-legacy.BX3IWSN6.js"];
      var styles = [];
      var fontPreconnectUrls = [];
      var fontPrefetchUrls = [];
      var imgPrefetchUrls = [];

      function preconnect(url, callback) {
        var link = document.createElement('link');
        link.rel = 'dns-prefetch preconnect';
        link.href = url;
        link.crossOrigin = '';
        link.onload = link.onerror = callback;
        document.head.appendChild(link);
      }

      function preconnectAssets() {
        var resources = preconnectOrigins.concat(fontPreconnectUrls);
        var index = 0;
        (function next() {
          var res = resources[index++];
          if (res) preconnect(res, next);
        })();
      }

      function prefetch(url, as, callback) {
        var link = document.createElement('link');
        if (link.relList.supports('prefetch')) {
          link.rel = 'prefetch';
          link.fetchPriority = 'low';
          link.as = as;
          if (as === 'font') link.type = 'font/woff2';
          link.href = url;
          link.crossOrigin = '';
          link.onload = link.onerror = callback;
          document.head.appendChild(link);
        } else {
          var xhr = new XMLHttpRequest();
          xhr.open('GET', url, true);
          xhr.onloadend = callback;
          xhr.send();
        }
      }

      function prefetchAssets() {
        var resources = [].concat(
          scripts.map(function(url) { return [url, 'script']; }),
          styles.map(function(url) { return [url, 'style']; }),
          fontPrefetchUrls.map(function(url) { return [url, 'font']; }),
          imgPrefetchUrls.map(function(url) { return [url, 'image']; })
        );
        var index = 0;
        function run() {
          var res = resources[index++];
          if (res) prefetch(res[0], res[1], next);
        }
        var next = (self.requestIdleCallback || setTimeout).bind(self, run);
        next();
      }

      function onLoaded() {
        try {
          if (parseFloat(navigator.connection.effectiveType) > 2 && !navigator.connection.saveData) {
            preconnectAssets();
            prefetchAssets();
          }
        } catch (e) {}
      }

      if (document.readyState === 'complete') {
        onLoaded();
      } else {
        addEventListener('load', onLoaded);
      }
    })();
  