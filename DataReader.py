<!DOCTYPE html>
<!-- saved from url=(0073)https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
  <link rel="dns-prefetch" href="https://github.githubassets.com/">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com/">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-qYFA4GyDouBDYZJ6KlTyq1ZDeeaf3DcN7b6s3SL9XSbvl9j2vRulhsLbPDDdil1/BqPMxDkdC++eHmjuzXL+4A==" rel="stylesheet" href="./DataReader_files/frameworks-a98140e06c83a2e04361927a2a54f2ab.css">
  
    <link crossorigin="anonymous" media="all" integrity="sha512-UXLlOs8jTGkaY4JzqtBBlrFoZO0y2J4kHlgRRUPvB5AjRyorrLyZgOTgk8LmBBKggjkoG7iYSzgw9qyfIhDpfw==" rel="stylesheet" href="./DataReader_files/behaviors-5172e53acf234c691a638273aad04196.css">
    
    
    
    <link crossorigin="anonymous" media="all" integrity="sha512-5NkcZ5jU9wXtJKTL/ZhHdiNZRDMUXeEn5cgjpuyZaXpB8I01Tp73dfH5Y0karRFEukoxlbvUWiP3crPxOlzDfQ==" rel="stylesheet" href="./DataReader_files/github-e4d91c6798d4f705ed24a4cbfd984776.css">

  <script crossorigin="anonymous" defer="defer" integrity="sha512-CzeY4A6TiG4fGZSWZU8FxmzFFmcQFoPpArF0hkH0/J/S7UL4eed/LKEXMQXfTwiG5yEJBI+9BdKG8KQJNbhcIQ==" type="application/javascript" src="./DataReader_files/environment-0b3798e0.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-IK3YFahDBTuoENbqq3ZAfDZnBrfSC3qdiUEGdRdDqm2HTSj2s9YynLxdZPgRJ5LXTvPR9jVkBCkz8PQRvaXb/A==" type="application/javascript" src="./DataReader_files/chunk-frameworks-20add815.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-YufdcMb4hh5uM2JSDx/MEATxourBQILRY0+74aM14JruGbjAyRYNY7hr/9+MOvY/ItDDo5pyqG/MHZr+5zZKHg==" type="application/javascript" src="./DataReader_files/chunk-vendor-62e7dd70.js.download"></script>
  
  <script crossorigin="anonymous" defer="defer" integrity="sha512-PsOLfdq6hGTzhE8a2IM8J1MyLGWBQj5m6+uGm5j+ypqMbR7sbGOo+NRMUPLqDBSwusFBeG38TXtz8WyGyszMJg==" type="application/javascript" src="./DataReader_files/behaviors-3ec38b7d.js.download"></script>
  
    <script crossorigin="anonymous" defer="defer" integrity="sha512-VuP/2HeHlwuxYb9sV0y9/hgN869dWIQDX2WZrvh4VAQjo6tb7PXzbBz0nOYROez0xFLxRc/u6sVU6fuYgcpN8w==" type="application/javascript" data-module-id="./chunk-animate-on-scroll.js" data-src="https://github.githubassets.com/assets/chunk-animate-on-scroll-56e3ffd8.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-ct3QiK2mvpg7zor9R2psdWnNMM2K32RU4RGRB/7yA5FyZ8H4iY6SNynXc7UaJqzBx6NaReg3GsWJPwW3kgAAig==" type="application/javascript" data-module-id="./chunk-codemirror.js" data-src="https://github.githubassets.com/assets/chunk-codemirror-72ddd088.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-9UuJ//O9hwCOI7MwzyVAJXn1D9B0WaQFktu5Qzw+7mg18URfaXXS7LsQVNirCGlgrmKe20UCtbj/4aGmw9Wk7g==" type="application/javascript" data-module-id="./chunk-color-modes.js" src="./DataReader_files/chunk-color-modes-f54b89ff.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-zkYZSjUFqSifB+Lt76jclFMrfqpcPqevT801RZcoBNCZHRTBKcFrW9OyJoPOzKFv+fZVDRnqdqGsuIv5KOIgZg==" type="application/javascript" data-module-id="./chunk-contributions-spider-graph.js" data-src="https://github.githubassets.com/assets/chunk-contributions-spider-graph-ce46194a.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-6j/oSF+kbW+yetNPvI684VzAu9pzug6Vj2h+3u1LdCuRhR4jnuiHZfeQKls3nxcT/S3H+oIt7FtigE/aeoj+gg==" type="application/javascript" data-module-id="./chunk-drag-drop.js" data-src="https://github.githubassets.com/assets/chunk-drag-drop-ea3fe848.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-VSSd+Yzi2iMS+pibY6hD/WdypxAEdob5F2RMKxuKcAHS2EpFYJPeTXoVxt0NXg03tfj2dka2mEtHS+vjpYSaDw==" type="application/javascript" data-module-id="./chunk-edit-hook-secret-element.js" data-src="https://github.githubassets.com/assets/chunk-edit-hook-secret-element-55249df9.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-N+ziqJjVMfWiqeVHdayDHpNRlG5HsF+cgV+pFnMDoTJuvBzgw+ndsepe4NcKAxIS3WMvzMaQcYmd2vrIaoAJVg==" type="application/javascript" data-module-id="./chunk-edit.js" src="./DataReader_files/chunk-edit-37ece2a8.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-aiqMIGGZGo8AQMjcoImKPMTsZVVRl6htCSY7BpRmpGPG/AF+Wq+P/Oj/dthWQOIk9cCNMPEas7O2zAR6oqn0tA==" type="application/javascript" data-module-id="./chunk-emoji-picker-element.js" data-src="https://github.githubassets.com/assets/chunk-emoji-picker-element-6a2a8c20.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-ejCT9r9E93nir+wK3PibZdMK0J3VXEkbwlgdnOnaUNoiJDI60BMtFt1QwjMU/rLXcjnH0xvgVFINGBFkzvTmRw==" type="application/javascript" data-module-id="./chunk-filter-input.js" data-src="https://github.githubassets.com/assets/chunk-filter-input-7a3093f6.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-Z1wcyOFQHzyMSPqp5DLKrobr3DN2Q6Dz31cfPtw4b2vPs9PX0PrxyDXHpTbIlcZ9qT1M1BNAypHKKw8Lp6Yx/Q==" type="application/javascript" data-module-id="./chunk-insights-graph.js" data-src="https://github.githubassets.com/assets/chunk-insights-graph-675c1cc8.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-4iRI95LO0kKcZLWUoOzqI6w8IVGppDVluR4dL7yyz8zgBu/7JAib0MkRN5LUVxXv0KIT6mQ2m5jbKa1NeZoD5A==" type="application/javascript" data-module-id="./chunk-invitations.js" data-src="https://github.githubassets.com/assets/chunk-invitations-e22448f7.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-Dhn0P9aANkDPzMxpqETLGel8ELkO93wrLFrMnEOSg8DguOxR7UNY1MyL3lexSVWo/ZZvme3kcWTaM6gw/DJW1w==" type="application/javascript" data-module-id="./chunk-jump-to.js" data-src="https://github.githubassets.com/assets/chunk-jump-to-0e19f43f.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-0DSZHh/iD27pAOXl4AWcxPqgRsJAVr1M8SnaN4gKYH2ZplPywvL5oalqN4Qj03FsB5Ll0pytD5kiTMibgGq0BA==" type="application/javascript" data-module-id="./chunk-launch-code-element.js" data-src="https://github.githubassets.com/assets/chunk-launch-code-element-d034991e.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-RduaLAviB2ygvRK/eX5iwzYO43ie7svrJ0rYJs06x7XqpRl/IK8PPBscBWM9Moo5Z86DK2iRLE2+aR7TJ5Uc2Q==" type="application/javascript" data-module-id="./chunk-metric-selection-element.js" data-src="https://github.githubassets.com/assets/chunk-metric-selection-element-45db9a2c.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-Lo0j1owPfYM0txt85KwGzF1PQJLvLFGbRJoASd5ZKMQAV9ZSDg5bVm5UWBAz7glGzw1pkiUD2bCMs2wqyf+CEA==" type="application/javascript" data-module-id="./chunk-notification-list-focus.js" src="./DataReader_files/chunk-notification-list-focus-2e8d23d6.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-ma0OOy3nj0c1cqBx0BkcmIFsLqcSZ+MIukQxyEFM/OWTzZpG+QMgOoWPAHZz43M6fyjAUG1jH6c/6LPiiKPCyw==" type="application/javascript" data-module-id="./chunk-profile-pins-element.js" data-src="https://github.githubassets.com/assets/chunk-profile-pins-element-99ad0e3b.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-/kPLzWIe41nxla5A+wcKKPIw4xiAsuITdjbXGVCycmUYnADfCids8FdV+TCA68gr4jAhKIws7flLpL12MoouBA==" type="application/javascript" data-module-id="./chunk-readme-toc-element.js" src="./DataReader_files/chunk-readme-toc-element-fe43cbcd.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-F0E2A5YYSz+7eA/RyQ/vYtJzeK2sjNyyneVBqru/CPoRXGBiAcJ2tpN2MWLxkNCqirt88h/BMCAF/7YTZ2qZJA==" type="application/javascript" data-module-id="./chunk-ref-selector.js" src="./DataReader_files/chunk-ref-selector-17413603.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-Zii9oRdZ6q2QDNjL5A+me7jwJjMLvs1NiQNHmajUZnn4t9shcBDb4F8l/PQZW26eYfe5065oM7lIOSmbMinA7Q==" type="application/javascript" data-module-id="./chunk-responsive-underlinenav.js" src="./DataReader_files/chunk-responsive-underlinenav-6628bda1.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-UUeOf6fdSNCh5PEil2eqo9JMci+9FbJ2YdzZ1rE8fFMYtanaPRRJSidxpPbnl16jxAuQo0QzosPRMKbiFuN0sQ==" type="application/javascript" data-module-id="./chunk-runner-groups.js" data-src="https://github.githubassets.com/assets/chunk-runner-groups-51478e7f.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-tk76eoSLUqXSVZ8ANzPprrOImFIV1zQ/VBV+WzG8ZjZpVPH8cLkMH/ur5HJB1lxx9/yo+V2wjDF96t4qfUwZLA==" type="application/javascript" data-module-id="./chunk-severity-calculator-element.js" data-src="https://github.githubassets.com/assets/chunk-severity-calculator-element-b64efa7a.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-fIq9Mn7jY/bHQXnsmh+VejpDnaO+d/FDxsp+4CuZtdNLrLuO+dQCjh+m6Yd8GCYD2Cy6DWbCEyM+mH2dkB2H9A==" type="application/javascript" data-module-id="./chunk-sortable-behavior.js" data-src="https://github.githubassets.com/assets/chunk-sortable-behavior-7c8abd32.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-WK8VXw3lfUQ/VRW0zlgKPhcMUqH0uTnB/KzePUPdZhCm/HpxfXXHKTGvj5C0Oex7+zbIM2ECzULbtTCT4ug3yg==" type="application/javascript" data-module-id="./chunk-toast.js" data-src="https://github.githubassets.com/assets/chunk-toast-58af155f.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-vgHJEmEJxNmHucGbVY8bEUoOYo5/ZwpQ69rU8Dld89daWJ54uad9lNptxq32F8pnbHhdngw9lohNEbMbjmj5AQ==" type="application/javascript" data-module-id="./chunk-tweetsodium.js" data-src="https://github.githubassets.com/assets/chunk-tweetsodium-be01c912.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-a+Pr9qPUoA3j8O0EiWfWwxWH4ZiB1fweLkYrjYlvyy/SeJbcjR1B4UyYjypFb9kvoy7I2bwXU9ctjZInmlyBXg==" type="application/javascript" data-module-id="./chunk-user-status-submit.js" data-src="https://github.githubassets.com/assets/chunk-user-status-submit-6be3ebf6.js"></script>
  
  <script crossorigin="anonymous" defer="defer" integrity="sha512-bS6dQhaUfxb3rXSLuEN+7HlkA3TzzfxqBkaSQaoSZLzje7r3H26uID+7rfjxpW10uj91kGL1n6uCh3JXO4+t5g==" type="application/javascript" src="./DataReader_files/repositories-6d2e9d42.js.download"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-LuxBgyY2ZOF1Yi1Hz1+o0TMTHvhTWdE1RwYP0dEg+O8Hy9Y34bM5U9IWzvMBA2v/JRF4wKCE+HPc72tAvINZOw==" type="application/javascript" src="./DataReader_files/diffs-2eec4183.js.download"></script>

  <meta name="viewport" content="width=device-width">
  
  <title>image-clustering/DataReader.py at master · ZeyadZanaty/image-clustering</title>
    <meta name="description" content="K-Means Clustering Implementation on CIFAR-10/CIFAR-100/MNIST Datasets - ZeyadZanaty/image-clustering">
    <link rel="search" type="application/opensearchdescription+xml" href="https://github.com/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">
  <meta name="apple-itunes-app" content="app-id=1477376905">
    <meta name="twitter:image:src" content="https://opengraph.githubassets.com/54d5725729eff13f82e34448dbf8be1c9308ecc5251d64c8d8dbb55d0df9898a/ZeyadZanaty/image-clustering"><meta name="twitter:site" content="@github"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="ZeyadZanaty/image-clustering"><meta name="twitter:description" content="K-Means Clustering Implementation on CIFAR-10/CIFAR-100/MNIST Datasets - ZeyadZanaty/image-clustering">
    <meta property="og:image" content="https://opengraph.githubassets.com/54d5725729eff13f82e34448dbf8be1c9308ecc5251d64c8d8dbb55d0df9898a/ZeyadZanaty/image-clustering"><meta property="og:image:alt" content="K-Means Clustering Implementation on CIFAR-10/CIFAR-100/MNIST Datasets - ZeyadZanaty/image-clustering"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="600"><meta property="og:site_name" content="GitHub"><meta property="og:type" content="object"><meta property="og:title" content="ZeyadZanaty/image-clustering"><meta property="og:url" content="https://github.com/ZeyadZanaty/image-clustering"><meta property="og:description" content="K-Means Clustering Implementation on CIFAR-10/CIFAR-100/MNIST Datasets - ZeyadZanaty/image-clustering">



    

  <link rel="assets" href="https://github.githubassets.com/">
  

  

    


  

  

  

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com"><meta name="octolytics-app-id" content="github"><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event">

  

  



  <meta name="optimizely-datafile" content="{&quot;version&quot;: &quot;4&quot;, &quot;rollouts&quot;: [], &quot;typedAudiences&quot;: [], &quot;anonymizeIP&quot;: true, &quot;projectId&quot;: &quot;16737760170&quot;, &quot;variables&quot;: [], &quot;featureFlags&quot;: [], &quot;experiments&quot;: [{&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;20106410318&quot;, &quot;key&quot;: &quot;en&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;20122000362&quot;, &quot;key&quot;: &quot;ko&quot;}], &quot;id&quot;: &quot;20121990335&quot;, &quot;key&quot;: &quot;ko_homepage_translation&quot;, &quot;layerId&quot;: &quot;20100420349&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;20106410318&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;20122000362&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {}}, {&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;20227754799&quot;, &quot;key&quot;: &quot;control&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;20233267869&quot;, &quot;key&quot;: &quot;treatment&quot;}], &quot;id&quot;: &quot;20194668672&quot;, &quot;key&quot;: &quot;recommended_plan_in_signup&quot;, &quot;layerId&quot;: &quot;20231804245&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;20233267869&quot;, &quot;endOfRange&quot;: 2500}, {&quot;entityId&quot;: &quot;&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;20227754799&quot;, &quot;endOfRange&quot;: 7500}, {&quot;entityId&quot;: &quot;&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {&quot;d0c8cbf56b61c99517936207d280de0c&quot;: &quot;treatment&quot;}}, {&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;20233300304&quot;, &quot;key&quot;: &quot;launch_code_variation&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;20227370325&quot;, &quot;key&quot;: &quot;control&quot;}], &quot;id&quot;: &quot;20206000276&quot;, &quot;key&quot;: &quot;launch_code_verification&quot;, &quot;layerId&quot;: &quot;20233240262&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;20233300304&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;20233300304&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {}}, {&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;20236992340&quot;, &quot;key&quot;: &quot;usd&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;20184442182&quot;, &quot;key&quot;: &quot;localized_currency&quot;}], &quot;id&quot;: &quot;20233233507&quot;, &quot;key&quot;: &quot;local_currency_pricing&quot;, &quot;layerId&quot;: &quot;20212472765&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;20184442182&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;20236992340&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {&quot;667685045.1617740930&quot;: &quot;localized_currency&quot;}}], &quot;audiences&quot;: [{&quot;conditions&quot;: &quot;[\&quot;or\&quot;, {\&quot;match\&quot;: \&quot;exact\&quot;, \&quot;name\&quot;: \&quot;$opt_dummy_attribute\&quot;, \&quot;type\&quot;: \&quot;custom_attribute\&quot;, \&quot;value\&quot;: \&quot;$opt_dummy_value\&quot;}]&quot;, &quot;id&quot;: &quot;$opt_dummy_audience&quot;, &quot;name&quot;: &quot;Optimizely-Generated Audience for Backwards Compatibility&quot;}], &quot;groups&quot;: [], &quot;attributes&quot;: [{&quot;id&quot;: &quot;16822470375&quot;, &quot;key&quot;: &quot;user_id&quot;}, {&quot;id&quot;: &quot;17143601254&quot;, &quot;key&quot;: &quot;spammy&quot;}, {&quot;id&quot;: &quot;18175660309&quot;, &quot;key&quot;: &quot;organization_plan&quot;}, {&quot;id&quot;: &quot;18813001570&quot;, &quot;key&quot;: &quot;is_logged_in&quot;}, {&quot;id&quot;: &quot;19073851829&quot;, &quot;key&quot;: &quot;geo&quot;}, {&quot;id&quot;: &quot;20175462351&quot;, &quot;key&quot;: &quot;requestedCurrency&quot;}], &quot;botFiltering&quot;: false, &quot;accountId&quot;: &quot;16737760170&quot;, &quot;events&quot;: [{&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;17911811441&quot;, &quot;key&quot;: &quot;hydro_click.dashboard.teacher_toolbox_cta&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18124116703&quot;, &quot;key&quot;: &quot;submit.organizations.complete_sign_up&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18145892387&quot;, &quot;key&quot;: &quot;no_metric.tracked_outside_of_optimizely&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18178755568&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.add_repo&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18180553241&quot;, &quot;key&quot;: &quot;submit.repository_imports.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18186103728&quot;, &quot;key&quot;: &quot;click.help.learn_more_about_repository_creation&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18188530140&quot;, &quot;key&quot;: &quot;test_event.do_not_use_in_production&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18191963644&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.transfer_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18195612788&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.import_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18210945499&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.invite_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18211063248&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.create_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18215721889&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.update_profile&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18224360785&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.dismiss&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18234832286&quot;, &quot;key&quot;: &quot;submit.organization_activation.complete&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18252392383&quot;, &quot;key&quot;: &quot;submit.org_repository.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18257551537&quot;, &quot;key&quot;: &quot;submit.org_member_invitation.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18259522260&quot;, &quot;key&quot;: &quot;submit.organization_profile.update&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18564603625&quot;, &quot;key&quot;: &quot;view.classroom_select_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18568612016&quot;, &quot;key&quot;: &quot;click.classroom_sign_in_click&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18572592540&quot;, &quot;key&quot;: &quot;view.classroom_name&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18574203855&quot;, &quot;key&quot;: &quot;click.classroom_create_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18582053415&quot;, &quot;key&quot;: &quot;click.classroom_select_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18589463420&quot;, &quot;key&quot;: &quot;click.classroom_create_classroom&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18591323364&quot;, &quot;key&quot;: &quot;click.classroom_create_first_classroom&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18591652321&quot;, &quot;key&quot;: &quot;click.classroom_grant_access&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18607131425&quot;, &quot;key&quot;: &quot;view.classroom_creation&quot;}, {&quot;experimentIds&quot;: [&quot;20194668672&quot;], &quot;id&quot;: &quot;18831680583&quot;, &quot;key&quot;: &quot;upgrade_account_plan&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19064064515&quot;, &quot;key&quot;: &quot;click.signup&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19075373687&quot;, &quot;key&quot;: &quot;click.view_account_billing_page&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19077355841&quot;, &quot;key&quot;: &quot;click.dismiss_signup_prompt&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19079713938&quot;, &quot;key&quot;: &quot;click.contact_sales&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19120963070&quot;, &quot;key&quot;: &quot;click.compare_account_plans&quot;}, {&quot;experimentIds&quot;: [&quot;20233233507&quot;], &quot;id&quot;: &quot;19151690317&quot;, &quot;key&quot;: &quot;click.upgrade_account_cta&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19424193129&quot;, &quot;key&quot;: &quot;click.open_account_switcher&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19520330825&quot;, &quot;key&quot;: &quot;click.visit_account_profile&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19540970635&quot;, &quot;key&quot;: &quot;click.switch_account_context&quot;}, {&quot;experimentIds&quot;: [&quot;20121990335&quot;], &quot;id&quot;: &quot;19730198868&quot;, &quot;key&quot;: &quot;submit.homepage_signup&quot;}, {&quot;experimentIds&quot;: [&quot;20121990335&quot;], &quot;id&quot;: &quot;19820830627&quot;, &quot;key&quot;: &quot;click.homepage_signup&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19988571001&quot;, &quot;key&quot;: &quot;click.create_enterprise_trial&quot;}, {&quot;experimentIds&quot;: [&quot;20233233507&quot;], &quot;id&quot;: &quot;20036538294&quot;, &quot;key&quot;: &quot;click.create_organization_team&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20040653299&quot;, &quot;key&quot;: &quot;click.input_enterprise_trial_form&quot;}, {&quot;experimentIds&quot;: [&quot;20233233507&quot;], &quot;id&quot;: &quot;20062030003&quot;, &quot;key&quot;: &quot;click.continue_with_team&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20068947153&quot;, &quot;key&quot;: &quot;click.create_organization_free&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20086636658&quot;, &quot;key&quot;: &quot;click.signup_continue.username&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20091648988&quot;, &quot;key&quot;: &quot;click.signup_continue.create_account&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20103637615&quot;, &quot;key&quot;: &quot;click.signup_continue.email&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20111574253&quot;, &quot;key&quot;: &quot;click.signup_continue.password&quot;}, {&quot;experimentIds&quot;: [&quot;20233233507&quot;], &quot;id&quot;: &quot;20120044111&quot;, &quot;key&quot;: &quot;view.pricing_page&quot;}, {&quot;experimentIds&quot;: [&quot;20121990335&quot;, &quot;20233233507&quot;], &quot;id&quot;: &quot;20152062109&quot;, &quot;key&quot;: &quot;submit.create_account&quot;}, {&quot;experimentIds&quot;: [&quot;20233233507&quot;], &quot;id&quot;: &quot;20165800992&quot;, &quot;key&quot;: &quot;submit.upgrade_payment_form&quot;}, {&quot;experimentIds&quot;: [&quot;20233233507&quot;], &quot;id&quot;: &quot;20171520319&quot;, &quot;key&quot;: &quot;submit.create_organization&quot;}, {&quot;experimentIds&quot;: [&quot;20194668672&quot;], &quot;id&quot;: &quot;20222645674&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.discuss_your_needs&quot;}, {&quot;experimentIds&quot;: [&quot;20206000276&quot;], &quot;id&quot;: &quot;20227443657&quot;, &quot;key&quot;: &quot;submit.verify_primary_user_email&quot;}, {&quot;experimentIds&quot;: [&quot;20194668672&quot;], &quot;id&quot;: &quot;20234607160&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.try_enterprise&quot;}, {&quot;experimentIds&quot;: [&quot;20194668672&quot;], &quot;id&quot;: &quot;20238175784&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.team&quot;}, {&quot;experimentIds&quot;: [&quot;20194668672&quot;], &quot;id&quot;: &quot;20239847212&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.continue_free&quot;}, {&quot;experimentIds&quot;: [&quot;20194668672&quot;], &quot;id&quot;: &quot;20251097193&quot;, &quot;key&quot;: &quot;recommended_plan&quot;}], &quot;revision&quot;: &quot;691&quot;}">
  <!-- To prevent page flashing, the optimizely JS needs to be loaded in the
    <head> tag before the DOM renders -->
  <script crossorigin="anonymous" defer="defer" integrity="sha512-yDmmCGyENqEePvF9X9A4omxWCNcbS6qK2h8HZPdnvXd02Vzhtqd0zRd/pgTgqQ/xOA02F3H225VpJvDXrnfNbA==" type="application/javascript" src="./DataReader_files/optimizely-c839a608.js.download"></script>



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="">


      <meta name="expected-hostname" content="github.com">


    <meta name="enabled-features" content="MARKETPLACE_PENDING_INSTALLATIONS,AUTOCOMPLETE_EMOJIS_IN_MARKDOWN_EDITOR">

  <meta http-equiv="x-pjax-version" content="ee17818d06d7779c8fba4876ea2694456a71fb4bb653520b38693cd427488cf3">
  

    
  <meta name="go-import" content="github.com/ZeyadZanaty/image-clustering git https://github.com/ZeyadZanaty/image-clustering.git">

  <meta name="octolytics-dimension-user_id" content="18510795"><meta name="octolytics-dimension-user_login" content="ZeyadZanaty"><meta name="octolytics-dimension-repository_id" content="161846877"><meta name="octolytics-dimension-repository_nwo" content="ZeyadZanaty/image-clustering"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="161846877"><meta name="octolytics-dimension-repository_network_root_nwo" content="ZeyadZanaty/image-clustering">



    


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="browser-optimizely-client-errors-url" content="https://api.github.com/_private/browser/optimizely_client/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark">


  <link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials">

<meta name="enabled-homepage-translation-languages" content="ko">

  <style type="text/css">@import url(https://fonts.googleapis.com/css?family=Lato:300,400,700,900);</style><style type="text/css">.huntr-ext-add-job-container .add-job-container {
  padding: 25px 25px 100px 25px;
  max-height: 550px;
}
.huntr-ext-add-job-container .save-job-footer {
  width: 300px;
  position: absolute;
  bottom: 22px;
  background-color: #f3f1f5;
  border-top: 1px solid rgba(0,0,0,0.1);
  border-bottom: 1px solid rgba(0,0,0,0.1);
}
.huntr-ext-add-job-container .btn {
  margin-left: auto !important;
  margin-right: auto !important;
  margin-top: 10px !important;
  margin-bottom: 10px !important;
  width: 150px !important;
}
.huntr-ext-add-job-container .btn.waiting {
  pointer-events: none;
  cursor: not-allowed;
}
.huntr-ext-add-job-container .list-item {
  text-transform: capitalize;
}
.huntr-ext-parsed-jobs-container .no-results {
  font-size: 14px !important;
  color: rgba(25,4,69,0.7) !important;
  padding: 40px;
  text-align: center;
}
.huntr-ext-parsed-jobs-container .job-result {
  padding: 20px 25px;
  border-bottom: 1px solid rgba(0,0,0,0.1);
  cursor: pointer;
}
.huntr-ext-parsed-jobs-container .job-result:hover {
  background-color: rgba(25,4,69,0.1);
}
.huntr-ext-parsed-jobs-container .job-title {
  font-size: 14px !important;
  font-weight: bold !important;
  color: #190445 !important;
  margin-bottom: 3px !important;
}
.huntr-ext-parsed-jobs-container .job-company,
.huntr-ext-parsed-jobs-container .job-location {
  max-width: 100px !important;
}
.huntr-ext-parsed-jobs-container .job-company {
  margin-right: 10px !important;
  font-weight: bold;
  color: rgba(25,4,69,0.9);
}
.huntr-ext-parsed-jobs-container .job-location {
  color: rgba(25,4,69,0.7);
}
.huntr-ext-parsed-jobs-container .job-description {
  color: rgba(25,4,69,0.4);
}
.huntr-ext-parsed-jobs-container .job-company,
.huntr-ext-parsed-jobs-container .job-description,
.huntr-ext-parsed-jobs-container .job-location {
  font-size: 13px;
}
.huntr-ext-parsed-jobs-container p {
  line-height: 15px !important;
  margin: 0 !important;
}
.huntr-ext-parsed-jobs-container span {
  margin: 0 !important;
  max-width: 240px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  display: inline-block;
}
.huntr-capitalize {
  text-transform: capitalize;
}
.huntr-error-footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  cursor: pointer;
  background-color: #ff3569;
  padding: 15px;
  font-size: 12px;
  color: #fff;
  border-top: 1px solid rgba(0,0,0,0.1);
  text-align: center;
  font-family: Lato, sans-serif;
}
.huntr-ext-add-job-success-container {
  padding: 30px;
  text-align: center;
}
.huntr-ext-add-job-success-container .message {
  height: 180px !important;
  margin-top: 20px !important;
  border-bottom: 1px solid #eaeaea !important;
}
.huntr-ext-add-job-success-container .message p {
  font-size: 22px !important;
  line-height: 50px !important;
  text-align: center !important;
}
.huntr-ext-add-job-success-container .message .huntr-icon {
  font-size: 45px !important;
  color: rgba(74,74,74,0.2) !important;
}
.huntr-ext-add-job-success-container .huntr-footer {
  margin-top: 30px;
}
.huntr-ext-add-job-success-container .huntr-footer a.btn {
  color: #fff !important;
  width: 200px;
}
.huntr-ext-add-job-success-container .huntr-footer .btn img {
  position: absolute;
  left: 8px;
  top: 7px;
  width: 20px;
  height: 20px;
  border-radius: 20px;
}
.huntr-ext-settings-container {
  margin-top: 25px;
  font-family: 'Lato', sans-serif !important;
  font-size: 16px;
  text-align: center;
  color: #4a4a4a;
  height: 140px;
  margin-top: 50px;
}
.huntr-ext-settings-container p {
  line-height: 18px;
}
.huntr-ext-time-to-upgrade {
  padding: 35px;
  text-align: center;
  color: #6a4feb;
}
.huntr-ext-time-to-upgrade .huntr-icon {
  margin: 10px 0 40px 0;
  font-size: 60px;
  color: rgba(106,79,235,0.1);
}
#huntr-react-container-2 {
  font-smoothing: antialiased;
  -webkit-font-smoothing: antialiased;
  position: absolute;
  display: block !important;
  font-family: 'Lato', sans-serif;
}
#huntr-react-container-2 a,
#huntr-react-container-2 p,
#huntr-react-container-2 span,
#huntr-react-container-2 div {
  font-family: 'Lato', sans-serif !important;
}
#huntr-react-container-2 form {
  margin: 0;
  padding: 0;
}
#huntr-react-container-2 ::-webkit-scrollbar-button {
  width: 0px !important;
  height: 0px !important;
}
#huntr-react-container-2 ::-webkit-scrollbar-track {
  box-shadow: none !important;
  background-color: "white" !important;
}
#huntr-react-container-2 ::-webkit-scrollbar-thumb {
  background-color: rgba(24,0,69,0.1) !important;
  border: 4px solid #fff !important;
  border-radius: 100px !important;
}
#huntr-react-container-2 ::-webkit-scrollbar-thumb:hover {
  background-color: rgba(24,0,69,0.2) !important;
}
#huntr-react-container-2 ::-webkit-scrollbar-thumb:active {
  background-color: rgba(24,0,69,0.2) !important;
}
#huntr-react-container-2 ::-webkit-scrollbar {
  width: 13px !important;
  height: 20px !important;
}
#huntr-react-container-2 .huntr-title {
  font-size: 22px;
  font-weight: regular;
  color: #190445 !important;
}
#huntr-react-container-2 .huntr-description {
  font-size: 15px;
  font-weight: regular;
  color: rgba(25,4,69,0.7) !important;
}
#huntr-react-container-2 a {
  cursor: pointer;
}
#huntr-react-container-2 .centered {
  margin-right: auto;
  margin-left: auto;
  text-align: center;
}
#huntr-react-container-2 .field {
  position: relative;
}
#huntr-react-container-2 .field-container .huntr-icon {
  position: absolute;
  right: 5px;
  bottom: 14px;
  font-size: 16px;
  color: #d4d4d4;
  cursor: pointer;
}
#huntr-react-container-2 .field-container .input-image {
  width: 20px;
  height: 20px;
  position: absolute;
  right: 5px;
  bottom: 14px;
  border-radius: 100%;
  box-shadow: 0px 0px 4px rgba(0,0,0,0.1);
}
#huntr-react-container-2 .hide {
  visibility: hidden;
}
#huntr-react-container-2 .btn {
  font-family: 'Lato', sans-serif !important;
  border-radius: 4px !important;
  font-size: 14px;
  display: block !important;
  cursor: pointer !important;
  text-transform: capitalize !important;
  font-weight: 400 !important;
  letter-spacing: 0.2px !important;
  position: relative;
  transition: all 0.4s ease-out !important;
  text-align: center !important;
  box-shadow: none !important;
  border: none !important;
  padding: 0 !important;
  background-image: none !important;
  background-repeat: no-repeat !important;
  text-shadow: none !important;
  line-height: 37px;
  box-sizing: border-box !important;
}
#huntr-react-container-2 .btn .huntr-icon {
  position: absolute;
  right: 15px;
  top: 13px;
  color: rgba(255,255,255,0.4);
  font-size: 16px;
}
#huntr-react-container-2 .btn-purple {
  color: #fff;
  text-shadow: 0px 1px 4px rgba(0,0,0,0.1);
  background-color: #6a4feb;
}
#huntr-react-container-2 .btn-purple:hover {
  background-color: #8c35ff;
}
#huntr-react-container-2 .btn-purple:disabled {
  cursor: not-allowed;
  color: rgba(25,4,69,0.4) !important;
  background-color: rgba(25,4,69,0.2) !important;
}
#huntr-react-container-2 ul {
  margin: 0px;
  padding: 0px;
}
#huntr-react-container-2 ul li {
  list-style: none;
}
#huntr-react-container-2 .location-search .huntr-drop-down-menu span {
  font-size: 11px;
  display: inline-block;
}
#huntr-react-container-2 .truncate {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
#huntr-react-container-2 .huntr-drop-down-menu {
  color: #4a4a4a;
  font-family: 'Lato', sans-serif;
  background-color: #fff;
  position: absolute;
  width: 100%;
  border-radius: 4px;
  font-size: 13px;
  box-shadow: 0px 0px 4px rgba(0,0,0,0.1);
  z-index: 1;
  border: 1px solid #ddd;
  max-height: 250px;
  overflow-y: auto;
}
#huntr-react-container-2 .huntr-drop-down-menu .huntr-ddmenu-footer {
  padding: 10px 10px;
  border-bottom: 1px solid #eee;
  text-align: left;
  cursor: pointer;
}
#huntr-react-container-2 .huntr-drop-down-menu .huntr-ddmenu-footer .huntr-icon {
  margin-right: 10px;
}
#huntr-react-container-2 .huntr-logo img {
  width: 16px;
  position: relative;
  top: -5px;
}
#huntr-react-container-2 .huntr-ext-nav-menu {
  width: 100%;
  position: relative;
  border-bottom: 1px solid rgba(0,0,0,0.1);
}
#huntr-react-container-2 .huntr-ext-nav-menu .nav-tooltip {
  display: none;
  position: absolute;
  background-color: #7f7b92;
  color: #fff;
  left: -45px;
  font-size: 11px;
  width: 90px;
  line-height: 30px;
  padding: 0px 15px;
  border-radius: 20px;
  top: -25px;
  text-align: center;
}
#huntr-react-container-2 .huntr-ext-nav-menu .nav-tooltip:before {
  content: '';
  display: block;
  width: 0;
  height: 0;
  position: absolute;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-top: 6px solid #7f7b92;
  top: 30px;
  left: 45px;
}
#huntr-react-container-2 .huntr-ext-nav-menu ul li {
  position: relative;
  padding: 0px;
  cursor: pointer;
  margin: 0px 31px 0px 0px;
  font-size: 17px;
  display: inline-block;
  color: #b5b5b5;
}
#huntr-react-container-2 .huntr-ext-nav-menu ul li a,
#huntr-react-container-2 .huntr-ext-nav-menu ul li span {
  line-height: 50px;
  vertical-align: middle;
}
#huntr-react-container-2 .huntr-ext-nav-menu ul li:first-child {
  margin-left: 20px;
}
#huntr-react-container-2 .huntr-ext-nav-menu ul li:last-child {
  margin: 0px;
}
#huntr-react-container-2 .huntr-ext-nav-menu ul li:hover {
  color: rgba(0,0,0,0.8);
}
#huntr-react-container-2 .huntr-ext-nav-menu ul li:hover .nav-tooltip {
  display: inline-block;
}
#huntr-react-container-2 .huntr-ext-top-menu {
  background-color: #f3f1f5;
  border-bottom: 1px solid rgba(0,0,0,0.1);
  position: relative;
  width: 100%;
  color: rgba(0,0,0,0.25);
}
#huntr-react-container-2 .huntr-ext-top-menu img {
  max-width: 60px;
  box-sizing: content-box;
  padding: 12px 0px 10px 12px;
}
#huntr-react-container-2 p,
#huntr-react-container-2 span {
  text-shadow: none;
}
#huntr-react-container-2 p.huntr-icon,
#huntr-react-container-2 span.huntr-icon {
  font-family: 'simple-line-icons' !important;
}
#huntr-react-container-2 p.huntr-icon:before,
#huntr-react-container-2 span.huntr-icon:before {
  font-family: 'simple-line-icons' !important;
}
#huntr-react-container-2 h1 {
  font-family: 'Lato', sans-serif !important;
  text-transform: uppercase !important;
  color: #4a4a4a !important;
  letter-spacing: 5px !important;
  font-size: 16px !important;
  font-weight: 900;
}
#huntr-react-container-2 .huntr-ext-app-container {
  position: fixed;
  right: 30px;
  top: 30px;
  z-index: 100000;
  max-height: 600px;
  min-height: 300px;
}
#huntr-react-container-2 .huntr-ext-app-container .inner-container {
  height: 100%;
  background-color: #fff;
  width: 300px;
  box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
  outline: 1px solid rgba(0,0,0,0.1);
}
#huntr-react-container-2 .huntr-ext-minimize {
  position: absolute;
  right: 10px;
  top: 0px;
  font-size: 35px;
  font-family: 'Lato', sans-serif;
  line-height: normal;
  transform: rotate(45deg);
  cursor: pointer;
  color: rgba(74,74,74,0.2);
  font-weight: 400;
  z-index: 1;
}
#huntr-react-container-2 .huntr-ext-minimize:hover {
  color: rgba(74,74,74,0.7);
}
#huntr-react-container-2 .editable-text-field {
  width: 100%;
}
#huntr-react-container-2 .huntr-ext-app-mini {
  background-color: #6a4feb;
  width: 50px;
  height: 50px;
  border-radius: 50px;
  position: fixed;
  z-index: 10000;
  bottom: 30px;
  right: 30px;
  cursor: pointer;
}
#huntr-react-container-2 .huntr-ext-app-mini:after {
  content: 'h';
}
#huntr-react-container-2 .huntr-ext-component-container h1 {
  text-align: center;
  margin: 60px 0px;
}
#huntr-react-container-2 .huntr-ext-component-container .drop-down-button {
  font-family: 'Lato', sans-serif !important;
  -webkit-appearance: none !important;
  outline: 0 !important;
  border-radius: 2px !important;
  box-sizing: border-box !important;
  font-family: 'Lato', sans-serif !important;
  width: 100% !important;
  padding: 12px 12px !important;
  font-size: 14px !important;
  color: rgba(74,74,74,0.9) !important;
  margin-bottom: 14px !important;
  font-weight: 400 !important;
  background-color: #fafafa !important;
  border: 1px solid #dcdcdc !important;
  transition: none !important;
  text-align: left !important;
  cursor: pointer !important;
}
#huntr-react-container-2 .huntr-ext-component-container input {
  font-size: 16px;
  height: 35px;
}
#huntr-react-container-2 .huntr-ext-component-container input::-webkit-input-placeholder {
  font-size: 16px !important;
  font-weight: 400 !important;
  font-family: 'Lato', sans-serif !important;
  color: rgba(24,0,69,0.3) !important;
}
#huntr-react-container-2 .huntr-ext-component-container textarea {
  font-size: 14px;
  height: 130px;
}
#huntr-react-container-2 .huntr-ext-component-container textarea::-webkit-input-placeholder {
  font-size: 14px !important;
  font-weight: 400 !important;
  font-family: 'Lato', sans-serif !important;
  color: rgba(24,0,69,0.3) !important;
}
#huntr-react-container-2 .huntr-ext-component-container input,
#huntr-react-container-2 .huntr-ext-component-container textarea {
  box-shadow: none;
  background-color: #fff;
  background-image: none !important;
  outline: 0;
  box-sizing: border-box;
  font-family: 'Lato', sans-serif !important;
  letter-spacing: 0px;
  width: 100%;
  border-top: none !important;
  border-left: none !important;
  border-right: none !important;
  box-shadow: none !important;
  border-bottom: 1px solid #eee !important;
  font-weight: 400 !important;
  margin: 0px !important;
  color: rgba(25,4,69,0.7) !important;
  border-radius: 0 !important;
  line-height: normal !important;
  padding: 20px 0 !important;
}
#huntr-react-container-2 .huntr-ext-component-container input.clean,
#huntr-react-container-2 .huntr-ext-component-container textarea.clean {
  border: none !important;
  height: 100%;
  padding: 0 !important;
}
#huntr-react-container-2 .huntr-ext-component-container input.clean:focus,
#huntr-react-container-2 .huntr-ext-component-container textarea.clean:focus,
#huntr-react-container-2 .huntr-ext-component-container input.clean::selection,
#huntr-react-container-2 .huntr-ext-component-container textarea.clean::selection {
  border-bottom: none !important;
}
#huntr-react-container-2 .huntr-ext-component-container input:focus,
#huntr-react-container-2 .huntr-ext-component-container textarea:focus,
#huntr-react-container-2 .huntr-ext-component-container input::selection,
#huntr-react-container-2 .huntr-ext-component-container textarea::selection {
  outline: 0;
  border-bottom: 1px solid #8c35ff !important;
  background-color: #fff !important;
}
#huntr-react-container-2 .huntr-ext-component-container input::selection,
#huntr-react-container-2 .huntr-ext-component-container textarea::selection {
  background-color: #8c35ff !important;
  color: #fff;
}
.huntr-loader ::after,
.huntr-loader ::before {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
.huntr-loader {
  display: block;
  height: 50px;
  width: 50px;
  animation: huntr-loader-1 3s linear infinite;
  -webkit-animation: huntr-loader-1 3s linear infinite;
}
@-webkit-keyframes huntr-loader-1 {
  0% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
  }
}
.huntr-loader span {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  height: 50px;
  width: 50px;
  clip: rect(0px, 50px, 50px, 0);
  -webkit-animation: huntr-loader-2 1.5s cubic-bezier(0.77, 0, 0.175, 1) infinite;
  animation: huntr-loader-2 1.5s cubic-bezier(0.77, 0, 0.175, 1) infinite;
}
@-webkit-keyframes huntr-loader-2 {
  0% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
  }
}
.huntr-loader span::before {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  height: 50px;
  width: 50px;
  border: 4px solid transparent;
  border-top: 4px solid #6a4feb;
  border-radius: 50%;
  -webkit-animation: huntr-loader-3 1.5s cubic-bezier(0.77, 0, 0.175, 1) infinite;
  animation: huntr-loader-3 1.5s cubic-bezier(0.77, 0, 0.175, 1) infinite;
}
@-webkit-keyframes huntr-loader-3 {
  0% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
  }
}
.huntr-loader span::after {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  height: 50px;
  width: 50px;
  border: 4px solid rgba(106,79,235,0.2);
  border-radius: 50%;
}
.react-datepicker-wrapper,
.react-datepicker__input-container {
  display: block !important;
}
.huntr-date-picker-popper {
  font-size: 0.8rem;
}
.huntr-date-picker-popper .react-datepicker {
  font-family: "Lato", Helvetica, Arial, sans-serif !important;
  background-color: #fff !important;
  color: #180045 !important;
  border: 1px solid rgba(24,0,69,0.1) !important;
  border-radius: 8px !important;
  box-shadow: 0px 3px 7px -1px rgba(24,0,69,0.1) !important;
}
.huntr-date-picker-popper .react-datepicker__header {
  background-color: #fafafb !important;
  border-bottom: 1px solid rgba(24,0,69,0.1) !important;
}
.huntr-date-picker-popper .react-datepicker__day {
  color: rgba(24,0,69,0.6) !important;
}
.huntr-date-picker-popper .react-datepicker__day-name {
  color: rgba(24,0,69,0.7) !important;
}
.huntr-date-picker-popper .react-datepicker__day--disabled {
  color: rgba(24,0,69,0.21) !important;
}
.huntr-date-picker-popper .react-datepicker__day--keyboard-selected,
.huntr-date-picker-popper .react-datepicker__day--selected {
  background-color: #8c35ff !important;
  color: #fff !important;
}
.huntr-date-picker-popper .react-datepicker__today-button {
  background-color: rgba(24,0,69,0.02) !important;
  border-top: 1px solid rgba(24,0,69,0.1) !important;
}
.huntr-date-picker-popper .react-datepicker__time-container--with-today-button {
  right: -96px !important;
  border: 1px solid rgba(24,0,69,0.1) !important;
  border-radius: 8px !important;
  box-shadow: 0px 3px 7px -1px rgba(24,0,69,0.1) !important;
}
.huntr-date-picker-popper .react-datepicker__time-list-item {
  color: rgba(24,0,69,0.7) !important;
  height: 18px !important;
}
.huntr-date-picker-popper .react-datepicker__time-list-item::hover {
  background-color: #fafafb !important;
}
.huntr-date-picker-popper .react-datepicker__time-list-item--selected {
  background-color: #8c35ff !important;
  color: #fff;
}
.huntr-date-picker {
  display: block;
}
.react-datepicker__close-icon {
  width: auto !important;
}
.react-datepicker__close-icon::after {
  background-color: #180045 !important;
  width: 12px !important;
  height: 12px !important;
}
@-moz-keyframes huntr-loader-1 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes huntr-loader-1 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@-o-keyframes huntr-loader-1 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@keyframes huntr-loader-1 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@-moz-keyframes huntr-loader-2 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes huntr-loader-2 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@-o-keyframes huntr-loader-2 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@keyframes huntr-loader-2 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@-moz-keyframes huntr-loader-3 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes huntr-loader-3 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@-o-keyframes huntr-loader-3 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@keyframes huntr-loader-3 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style><style type="text/css">/*!
 * Quill Editor v1.3.0
 * https://quilljs.com/
 * Copyright (c) 2014, Jason Chen
 * Copyright (c) 2013, salesforce.com
 */
#huntr-react-container-2 .ql-container span,
#huntr-react-container-2 .ql-container li,
#huntr-react-container-2 .ql-container ul,
#huntr-react-container-2 .ql-container div,
#huntr-react-container-2 .ql-container strong,
#huntr-react-container-2 .ql-container b,
#huntr-react-container-2 .ql-container h1,
#huntr-react-container-2 .ql-container h2,
#huntr-react-container-2 .ql-container h3,
#huntr-react-container-2 .ql-container p  {
  font-size: 14px;
  font-family: Lato, Arial, sans-serif !important;
  color: #180045 !important;
}

#huntr-react-container-2 .ql-container {
  box-sizing: border-box;
  font-family: Lato, Arial, sans-serif;
  font-size: 13px;
  height: 100%;
  margin: 0px;
  position: relative;
}
#huntr-react-container-2 .ql-container.ql-disabled .ql-tooltip {
  visibility: hidden;
}
#huntr-react-container-2 .ql-container.ql-disabled .ql-editor ul[data-checked] > li::before {
  pointer-events: none;
}
#huntr-react-container-2 .ql-clipboard {
  left: -100000px;
  height: 1px;
  overflow-y: hidden;
  position: absolute;
  top: 50%;
}
#huntr-react-container-2 .ql-clipboard p {
  margin: 0;
  padding: 0;
}
#huntr-react-container-2 .ql-editor {
  box-sizing: border-box;
  line-height: 1.42;
  height: 100% !important;
  outline: none;
  overflow-y: auto;
  padding: 12px 18px;
  tab-size: 4;
  -moz-tab-size: 4;
  text-align: left;
  white-space: pre-wrap;
  word-wrap: break-word;
}
#huntr-react-container-2 .ql-editor > * {
  cursor: text;
}
#huntr-react-container-2 .ql-editor p,
#huntr-react-container-2 .ql-editor ol,
#huntr-react-container-2 .ql-editor ul,
#huntr-react-container-2 .ql-editor pre,
#huntr-react-container-2 .ql-editor blockquote,
#huntr-react-container-2 .ql-editor h1,
#huntr-react-container-2 .ql-editor h2,
#huntr-react-container-2 .ql-editor h3,
#huntr-react-container-2 .ql-editor h4,
#huntr-react-container-2 .ql-editor h5,
#huntr-react-container-2 .ql-editor h6 {
  margin: 0;
  padding: 0;
  counter-reset: list-1 list-2 list-3 list-4 list-5 list-6 list-7 list-8 list-9;
}
#huntr-react-container-2 .ql-editor ol,
#huntr-react-container-2 .ql-editor ul {
  padding-left: 1.5em;
}
#huntr-react-container-2 .ql-editor ol > li,
#huntr-react-container-2 .ql-editor ul > li {
  list-style-type: none;
}
#huntr-react-container-2 .ql-editor ul > li::before {
  content: '\2022';
}
#huntr-react-container-2 .ql-editor ul[data-checked=true],
#huntr-react-container-2 .ql-editor ul[data-checked=false] {
  pointer-events: none;
}
#huntr-react-container-2 .ql-editor ul[data-checked=true] > li *,
#huntr-react-container-2 .ql-editor ul[data-checked=false] > li * {
  pointer-events: all;
}
#huntr-react-container-2 .ql-editor ul[data-checked=true] > li::before,
#huntr-react-container-2 .ql-editor ul[data-checked=false] > li::before {
  color: #777;
  cursor: pointer;
  pointer-events: all;
}
#huntr-react-container-2 .ql-editor ul[data-checked=true] > li::before {
  content: '\2611';
}
#huntr-react-container-2 .ql-editor ul[data-checked=false] > li::before {
  content: '\2610';
}
#huntr-react-container-2 .ql-editor li::before {
  display: inline-block;
  white-space: nowrap;
  width: 1.2em;
}
#huntr-react-container-2 .ql-editor li:not(.ql-direction-rtl)::before {
  margin-left: -1.5em;
  margin-right: 0.3em;
  text-align: right;
}
#huntr-react-container-2 .ql-editor li.ql-direction-rtl::before {
  margin-left: 0.3em;
  margin-right: -1.5em;
}
#huntr-react-container-2 .ql-editor ol li:not(.ql-direction-rtl),
#huntr-react-container-2 .ql-editor ul li:not(.ql-direction-rtl) {
  padding-left: 1.5em;
}
#huntr-react-container-2 .ql-editor ol li.ql-direction-rtl,
#huntr-react-container-2 .ql-editor ul li.ql-direction-rtl {
  padding-right: 1.5em;
}
#huntr-react-container-2 .ql-editor ol li {
  counter-reset: list-1 list-2 list-3 list-4 list-5 list-6 list-7 list-8 list-9;
  counter-increment: list-0;
}
#huntr-react-container-2 .ql-editor ol li:before {
  content: counter(list-0, decimal) '. ';
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-1 {
  counter-increment: list-1;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-1:before {
  content: counter(list-1, lower-alpha) '. ';
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-1 {
  counter-reset: list-2 list-3 list-4 list-5 list-6 list-7 list-8 list-9;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-2 {
  counter-increment: list-2;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-2:before {
  content: counter(list-2, lower-roman) '. ';
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-2 {
  counter-reset: list-3 list-4 list-5 list-6 list-7 list-8 list-9;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-3 {
  counter-increment: list-3;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-3:before {
  content: counter(list-3, decimal) '. ';
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-3 {
  counter-reset: list-4 list-5 list-6 list-7 list-8 list-9;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-4 {
  counter-increment: list-4;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-4:before {
  content: counter(list-4, lower-alpha) '. ';
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-4 {
  counter-reset: list-5 list-6 list-7 list-8 list-9;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-5 {
  counter-increment: list-5;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-5:before {
  content: counter(list-5, lower-roman) '. ';
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-5 {
  counter-reset: list-6 list-7 list-8 list-9;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-6 {
  counter-increment: list-6;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-6:before {
  content: counter(list-6, decimal) '. ';
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-6 {
  counter-reset: list-7 list-8 list-9;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-7 {
  counter-increment: list-7;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-7:before {
  content: counter(list-7, lower-alpha) '. ';
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-7 {
  counter-reset: list-8 list-9;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-8 {
  counter-increment: list-8;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-8:before {
  content: counter(list-8, lower-roman) '. ';
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-8 {
  counter-reset: list-9;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-9 {
  counter-increment: list-9;
}
#huntr-react-container-2 .ql-editor ol li.ql-indent-9:before {
  content: counter(list-9, decimal) '. ';
}
#huntr-react-container-2 .ql-editor .ql-indent-1:not(.ql-direction-rtl) {
  padding-left: 3em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-1:not(.ql-direction-rtl) {
  padding-left: 4.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-1.ql-direction-rtl.ql-align-right {
  padding-right: 3em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-1.ql-direction-rtl.ql-align-right {
  padding-right: 4.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-2:not(.ql-direction-rtl) {
  padding-left: 6em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-2:not(.ql-direction-rtl) {
  padding-left: 7.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-2.ql-direction-rtl.ql-align-right {
  padding-right: 6em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-2.ql-direction-rtl.ql-align-right {
  padding-right: 7.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-3:not(.ql-direction-rtl) {
  padding-left: 9em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-3:not(.ql-direction-rtl) {
  padding-left: 10.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-3.ql-direction-rtl.ql-align-right {
  padding-right: 9em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-3.ql-direction-rtl.ql-align-right {
  padding-right: 10.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-4:not(.ql-direction-rtl) {
  padding-left: 12em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-4:not(.ql-direction-rtl) {
  padding-left: 13.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-4.ql-direction-rtl.ql-align-right {
  padding-right: 12em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-4.ql-direction-rtl.ql-align-right {
  padding-right: 13.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-5:not(.ql-direction-rtl) {
  padding-left: 15em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-5:not(.ql-direction-rtl) {
  padding-left: 16.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-5.ql-direction-rtl.ql-align-right {
  padding-right: 15em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-5.ql-direction-rtl.ql-align-right {
  padding-right: 16.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-6:not(.ql-direction-rtl) {
  padding-left: 18em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-6:not(.ql-direction-rtl) {
  padding-left: 19.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-6.ql-direction-rtl.ql-align-right {
  padding-right: 18em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-6.ql-direction-rtl.ql-align-right {
  padding-right: 19.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-7:not(.ql-direction-rtl) {
  padding-left: 21em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-7:not(.ql-direction-rtl) {
  padding-left: 22.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-7.ql-direction-rtl.ql-align-right {
  padding-right: 21em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-7.ql-direction-rtl.ql-align-right {
  padding-right: 22.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-8:not(.ql-direction-rtl) {
  padding-left: 24em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-8:not(.ql-direction-rtl) {
  padding-left: 25.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-8.ql-direction-rtl.ql-align-right {
  padding-right: 24em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-8.ql-direction-rtl.ql-align-right {
  padding-right: 25.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-9:not(.ql-direction-rtl) {
  padding-left: 27em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-9:not(.ql-direction-rtl) {
  padding-left: 28.5em;
}
#huntr-react-container-2 .ql-editor .ql-indent-9.ql-direction-rtl.ql-align-right {
  padding-right: 27em;
}
#huntr-react-container-2 .ql-editor li.ql-indent-9.ql-direction-rtl.ql-align-right {
  padding-right: 28.5em;
}
#huntr-react-container-2 .ql-editor .ql-video {
  display: block;
  max-width: 100%;
}
#huntr-react-container-2 .ql-editor .ql-video.ql-align-center {
  margin: 0 auto;
}
#huntr-react-container-2 .ql-editor .ql-video.ql-align-right {
  margin: 0 0 0 auto;
}
#huntr-react-container-2 .ql-editor .ql-bg-black {
  background-color: #000;
}
#huntr-react-container-2 .ql-editor .ql-bg-red {
  background-color: #e60000;
}
#huntr-react-container-2 .ql-editor .ql-bg-orange {
  background-color: #f90;
}
#huntr-react-container-2 .ql-editor .ql-bg-yellow {
  background-color: #ff0;
}
#huntr-react-container-2 .ql-editor .ql-bg-green {
  background-color: #008a00;
}
#huntr-react-container-2 .ql-editor .ql-bg-blue {
  background-color: #06c;
}
#huntr-react-container-2 .ql-editor .ql-bg-purple {
  background-color: #93f;
}
#huntr-react-container-2 .ql-editor .ql-color-white {
  color: #fff;
}
#huntr-react-container-2 .ql-editor .ql-color-red {
  color: #e60000;
}
#huntr-react-container-2 .ql-editor .ql-color-orange {
  color: #f90;
}
#huntr-react-container-2 .ql-editor .ql-color-yellow {
  color: #ff0;
}
#huntr-react-container-2 .ql-editor .ql-color-green {
  color: #008a00;
}
#huntr-react-container-2 .ql-editor .ql-color-blue {
  color: #06c;
}
#huntr-react-container-2 .ql-editor .ql-color-purple {
  color: #93f;
}
#huntr-react-container-2 .ql-editor .ql-font-serif {
  font-family: Georgia, Times New Roman, serif;
}
#huntr-react-container-2 .ql-editor .ql-font-monospace {
  font-family: Monaco, Courier New, monospace;
}
#huntr-react-container-2 .ql-editor .ql-size-small {
  font-size: 0.75em;
}
#huntr-react-container-2 .ql-editor .ql-size-large {
  font-size: 1.5em;
}
#huntr-react-container-2 .ql-editor .ql-size-huge {
  font-size: 2.5em;
}
#huntr-react-container-2 .ql-editor .ql-direction-rtl {
  direction: rtl;
  text-align: inherit;
}
#huntr-react-container-2 .ql-editor .ql-align-center {
  text-align: center;
}
#huntr-react-container-2 .ql-editor .ql-align-justify {
  text-align: justify;
}
#huntr-react-container-2 .ql-editor .ql-align-right {
  text-align: right;
}
#huntr-react-container-2 .ql-editor .ql-embed-selected {
  border: 1px solid #777;
  user-select: none;
}
#huntr-react-container-2 .ql-editor.ql-blank::before {
  color: rgba(25,4,69,0.4);
  content: attr(data-placeholder);
  font-style: normal;
  pointer-events: none;
  position: absolute;
}
#huntr-react-container-2 .ql-snow.ql-toolbar:after,
#huntr-react-container-2 .ql-snow .ql-toolbar:after {
  clear: both;
  content: '';
  display: table;
}
#huntr-react-container-2 .ql-snow.ql-toolbar button,
#huntr-react-container-2 .ql-snow .ql-toolbar button {
  background: none;
  border: none;
  cursor: pointer;
  display: inline-block;
  float: left;
  height: 24px;
  padding: 3px 5px;
  width: 28px;
  box-shadow: none;
  min-height: 1em;
}
#huntr-react-container-2 .ql-snow.ql-toolbar button svg,
#huntr-react-container-2 .ql-snow .ql-toolbar button svg {
  float: left;
  height: 100%;
}
#huntr-react-container-2 .ql-snow.ql-toolbar button:active:hover,
#huntr-react-container-2 .ql-snow .ql-toolbar button:active:hover {
  outline: none;
}
#huntr-react-container-2 .ql-snow.ql-toolbar input.ql-image[type=file],
#huntr-react-container-2 .ql-snow .ql-toolbar input.ql-image[type=file] {
  display: none;
}
#huntr-react-container-2 .ql-snow.ql-toolbar button:hover,
#huntr-react-container-2 .ql-snow .ql-toolbar button:hover,
#huntr-react-container-2 .ql-snow.ql-toolbar button:focus,
#huntr-react-container-2 .ql-snow .ql-toolbar button:focus,
#huntr-react-container-2 .ql-snow.ql-toolbar button.ql-active,
#huntr-react-container-2 .ql-snow .ql-toolbar button.ql-active,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-label:hover,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-label:hover,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-label.ql-active,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-label.ql-active,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-item:hover,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-item:hover,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-item.ql-selected,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-item.ql-selected {
  color: #06c;
}
#huntr-react-container-2 .ql-snow.ql-toolbar button:hover .ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar button:hover .ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar button:focus .ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar button:focus .ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar button.ql-active .ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar button.ql-active .ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-label:hover .ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-label:hover .ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-label.ql-active .ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-label.ql-active .ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-item:hover .ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-item:hover .ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-item.ql-selected .ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-item.ql-selected .ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar button:hover .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar button:hover .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar button:focus .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar button:focus .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar button.ql-active .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar button.ql-active .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-label:hover .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-label:hover .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-label.ql-active .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-label.ql-active .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-item:hover .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-item:hover .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-item.ql-selected .ql-stroke.ql-fill,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-item.ql-selected .ql-stroke.ql-fill {
  fill: #06c;
}
#huntr-react-container-2 .ql-snow.ql-toolbar button:hover .ql-stroke,
#huntr-react-container-2 .ql-snow .ql-toolbar button:hover .ql-stroke,
#huntr-react-container-2 .ql-snow.ql-toolbar button:focus .ql-stroke,
#huntr-react-container-2 .ql-snow .ql-toolbar button:focus .ql-stroke,
#huntr-react-container-2 .ql-snow.ql-toolbar button.ql-active .ql-stroke,
#huntr-react-container-2 .ql-snow .ql-toolbar button.ql-active .ql-stroke,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-label:hover .ql-stroke,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-label:hover .ql-stroke,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-label.ql-active .ql-stroke,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-label.ql-active .ql-stroke,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-item:hover .ql-stroke,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-item:hover .ql-stroke,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-item.ql-selected .ql-stroke,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-item.ql-selected .ql-stroke,
#huntr-react-container-2 .ql-snow.ql-toolbar button:hover .ql-stroke-miter,
#huntr-react-container-2 .ql-snow .ql-toolbar button:hover .ql-stroke-miter,
#huntr-react-container-2 .ql-snow.ql-toolbar button:focus .ql-stroke-miter,
#huntr-react-container-2 .ql-snow .ql-toolbar button:focus .ql-stroke-miter,
#huntr-react-container-2 .ql-snow.ql-toolbar button.ql-active .ql-stroke-miter,
#huntr-react-container-2 .ql-snow .ql-toolbar button.ql-active .ql-stroke-miter,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-label:hover .ql-stroke-miter,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-label:hover .ql-stroke-miter,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-label.ql-active .ql-stroke-miter,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-label.ql-active .ql-stroke-miter,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-item:hover .ql-stroke-miter,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-item:hover .ql-stroke-miter,
#huntr-react-container-2 .ql-snow.ql-toolbar .ql-picker-item.ql-selected .ql-stroke-miter,
#huntr-react-container-2 .ql-snow .ql-toolbar .ql-picker-item.ql-selected .ql-stroke-miter {
  stroke: #06c;
}
@media (pointer: coarse) {
  .ql-snow.ql-toolbar button:hover:not(.ql-active),
  .ql-snow .ql-toolbar button:hover:not(.ql-active) {
    color: #444;
  }
  .ql-snow.ql-toolbar button:hover:not(.ql-active) .ql-fill,
  .ql-snow .ql-toolbar button:hover:not(.ql-active) .ql-fill,
  .ql-snow.ql-toolbar button:hover:not(.ql-active) .ql-stroke.ql-fill,
  .ql-snow .ql-toolbar button:hover:not(.ql-active) .ql-stroke.ql-fill {
    fill: #444;
  }
  .ql-snow.ql-toolbar button:hover:not(.ql-active) .ql-stroke,
  .ql-snow .ql-toolbar button:hover:not(.ql-active) .ql-stroke,
  .ql-snow.ql-toolbar button:hover:not(.ql-active) .ql-stroke-miter,
  .ql-snow .ql-toolbar button:hover:not(.ql-active) .ql-stroke-miter {
    stroke: #444;
  }
}
#huntr-react-container-2 .ql-snow {
  box-sizing: border-box;
}
#huntr-react-container-2 .ql-snow * {
  box-sizing: border-box;
}
#huntr-react-container-2 .ql-snow .ql-hidden {
  display: none;
}
#huntr-react-container-2 .ql-snow .ql-out-bottom,
#huntr-react-container-2 .ql-snow .ql-out-top {
  visibility: hidden;
}
#huntr-react-container-2 .ql-snow .ql-tooltip {
  position: absolute;
  transform: translateY(10px);
}
#huntr-react-container-2 .ql-snow .ql-tooltip a {
  cursor: pointer;
  text-decoration: none;
}
#huntr-react-container-2 .ql-snow .ql-tooltip.ql-flip {
  transform: translateY(-10px);
}
#huntr-react-container-2 .ql-snow .ql-formats {
  display: inline-block;
  vertical-align: middle;
}
#huntr-react-container-2 .ql-snow .ql-formats:after {
  clear: both;
  content: '';
  display: table;
}
#huntr-react-container-2 .ql-snow .ql-stroke {
  fill: none;
  stroke: #444;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-width: 2;
}
#huntr-react-container-2 .ql-snow .ql-stroke-miter {
  fill: none;
  stroke: #444;
  stroke-miterlimit: 10;
  stroke-width: 2;
}
#huntr-react-container-2 .ql-snow .ql-fill,
#huntr-react-container-2 .ql-snow .ql-stroke.ql-fill {
  fill: #444;
}
#huntr-react-container-2 .ql-snow .ql-empty {
  fill: none;
}
#huntr-react-container-2 .ql-snow .ql-even {
  fill-rule: evenodd;
}
#huntr-react-container-2 .ql-snow .ql-thin,
#huntr-react-container-2 .ql-snow .ql-stroke.ql-thin {
  stroke-width: 1;
}
#huntr-react-container-2 .ql-snow .ql-transparent {
  opacity: 0.4;
}
#huntr-react-container-2 .ql-snow .ql-direction svg:last-child {
  display: none;
}
#huntr-react-container-2 .ql-snow .ql-direction.ql-active svg:last-child {
  display: inline;
}
#huntr-react-container-2 .ql-snow .ql-direction.ql-active svg:first-child {
  display: none;
}
#huntr-react-container-2 .ql-snow .ql-editor h1 {
  font-size: 2em;
}
#huntr-react-container-2 .ql-snow .ql-editor h2 {
  font-size: 1.5em;
}
#huntr-react-container-2 .ql-snow .ql-editor h3 {
  font-size: 1.17em;
}
#huntr-react-container-2 .ql-snow .ql-editor h4 {
  font-size: 1em;
}
#huntr-react-container-2 .ql-snow .ql-editor h5 {
  font-size: 0.83em;
}
#huntr-react-container-2 .ql-snow .ql-editor h6 {
  font-size: 0.67em;
}
#huntr-react-container-2 .ql-snow .ql-editor a {
  text-decoration: underline;
}
#huntr-react-container-2 .ql-snow .ql-editor blockquote {
  border-left: 4px solid #ccc;
  margin-bottom: 5px;
  margin-top: 5px;
  padding-left: 16px;
}
#huntr-react-container-2 .ql-snow .ql-editor code,
#huntr-react-container-2 .ql-snow .ql-editor pre {
  background-color: #f0f0f0;
  border-radius: 3px;
}
#huntr-react-container-2 .ql-snow .ql-editor pre {
  white-space: pre-wrap;
  margin-bottom: 5px;
  margin-top: 5px;
  padding: 5px 10px;
}
#huntr-react-container-2 .ql-snow .ql-editor code {
  font-size: 85%;
  padding-bottom: 2px;
  padding-top: 2px;
}
#huntr-react-container-2 .ql-snow .ql-editor code:before,
#huntr-react-container-2 .ql-snow .ql-editor code:after {
  content: "\A0";
  letter-spacing: -2px;
}
#huntr-react-container-2 .ql-snow .ql-editor pre.ql-syntax {
  background-color: #23241f;
  color: #f8f8f2;
  overflow: visible;
}
#huntr-react-container-2 .ql-snow .ql-editor img {
  max-width: 100%;
}
#huntr-react-container-2 .ql-snow .ql-picker {
  color: #444;
  display: inline-block;
  float: left;
  font-size: 14px;
  font-weight: 500;
  height: 24px;
  position: relative;
  vertical-align: middle;
}
#huntr-react-container-2 .ql-snow .ql-picker-label {
  cursor: pointer;
  display: inline-block;
  height: 100%;
  padding-left: 8px;
  padding-right: 2px;
  position: relative;
  width: 100%;
}
#huntr-react-container-2 .ql-snow .ql-picker-label::before {
  display: inline-block;
  line-height: 22px;
}
#huntr-react-container-2 .ql-snow .ql-picker-options {
  background-color: #fff;
  display: none;
  min-width: 100%;
  padding: 4px 8px;
  position: absolute;
  white-space: nowrap;
}
#huntr-react-container-2 .ql-snow .ql-picker-options .ql-picker-item {
  cursor: pointer;
  display: block;
  padding-bottom: 5px;
  padding-top: 5px;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-expanded .ql-picker-label {
  color: #ccc;
  z-index: 2;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-expanded .ql-picker-label .ql-fill {
  fill: #ccc;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-expanded .ql-picker-label .ql-stroke {
  stroke: #ccc;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-expanded .ql-picker-options {
  display: block;
  margin-top: -1px;
  top: 100%;
  z-index: 1;
}
#huntr-react-container-2 .ql-snow .ql-color-picker,
#huntr-react-container-2 .ql-snow .ql-icon-picker {
  width: 28px;
}
#huntr-react-container-2 .ql-snow .ql-color-picker .ql-picker-label,
#huntr-react-container-2 .ql-snow .ql-icon-picker .ql-picker-label {
  padding: 2px 4px;
}
#huntr-react-container-2 .ql-snow .ql-color-picker .ql-picker-label svg,
#huntr-react-container-2 .ql-snow .ql-icon-picker .ql-picker-label svg {
  right: 4px;
}
#huntr-react-container-2 .ql-snow .ql-icon-picker .ql-picker-options {
  padding: 4px 0px;
}
#huntr-react-container-2 .ql-snow .ql-icon-picker .ql-picker-item {
  height: 24px;
  width: 24px;
  padding: 2px 4px;
}
#huntr-react-container-2 .ql-snow .ql-color-picker .ql-picker-options {
  padding: 3px 5px;
  width: 152px;
}
#huntr-react-container-2 .ql-snow .ql-color-picker .ql-picker-item {
  border: 1px solid transparent;
  float: left;
  height: 16px;
  margin: 2px;
  padding: 0px;
  width: 16px;
}
#huntr-react-container-2 .ql-snow .ql-picker:not(.ql-color-picker):not(.ql-icon-picker) svg {
  position: absolute;
  margin-top: -9px;
  right: 0;
  top: 50%;
  width: 18px;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-label[data-label]:not([data-label=''])::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-font .ql-picker-label[data-label]:not([data-label=''])::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-label[data-label]:not([data-label=''])::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-label]:not([data-label=''])::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-font .ql-picker-item[data-label]:not([data-label=''])::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-item[data-label]:not([data-label=''])::before {
  content: attr(data-label);
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header {
  width: 98px;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-label::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item::before {
  content: 'Normal';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-label[data-value="1"]::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="1"]::before {
  content: 'Heading 1';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-label[data-value="2"]::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="2"]::before {
  content: 'Heading 2';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-label[data-value="3"]::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="3"]::before {
  content: 'Heading 3';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-label[data-value="4"]::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="4"]::before {
  content: 'Heading 4';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-label[data-value="5"]::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="5"]::before {
  content: 'Heading 5';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-label[data-value="6"]::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="6"]::before {
  content: 'Heading 6';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="1"]::before {
  font-size: 2em;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="2"]::before {
  font-size: 1.5em;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="3"]::before {
  font-size: 1.17em;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="4"]::before {
  font-size: 1em;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="5"]::before {
  font-size: 0.83em;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-header .ql-picker-item[data-value="6"]::before {
  font-size: 0.67em;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-font {
  width: 108px;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-font .ql-picker-label::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-font .ql-picker-item::before {
  content: 'Sans Serif';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-font .ql-picker-label[data-value=serif]::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-font .ql-picker-item[data-value=serif]::before {
  content: 'Serif';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-font .ql-picker-label[data-value=monospace]::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-font .ql-picker-item[data-value=monospace]::before {
  content: 'Monospace';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-font .ql-picker-item[data-value=serif]::before {
  font-family: Georgia, Times New Roman, serif;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-font .ql-picker-item[data-value=monospace]::before {
  font-family: Monaco, Courier New, monospace;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-size {
  width: 98px;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-label::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-item::before {
  content: 'Normal';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-label[data-value=small]::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-item[data-value=small]::before {
  content: 'Small';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-label[data-value=large]::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-item[data-value=large]::before {
  content: 'Large';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-label[data-value=huge]::before,
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-item[data-value=huge]::before {
  content: 'Huge';
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-item[data-value=small]::before {
  font-size: 10px;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-item[data-value=large]::before {
  font-size: 18px;
}
#huntr-react-container-2 .ql-snow .ql-picker.ql-size .ql-picker-item[data-value=huge]::before {
  font-size: 32px;
}
#huntr-react-container-2 .ql-snow .ql-color-picker.ql-background .ql-picker-item {
  background-color: #fff;
}
#huntr-react-container-2 .ql-snow .ql-color-picker.ql-color .ql-picker-item {
  background-color: #000;
}
#huntr-react-container-2 .ql-toolbar.ql-snow {
  border-bottom: 1px solid #ECE9F2;
  box-sizing: border-box;
  font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
  padding: 8px;
}
#huntr-react-container-2 .ql-toolbar.ql-snow .ql-formats {
  margin-right: 15px;
}
#huntr-react-container-2 .ql-toolbar.ql-snow .ql-picker-label {
  border: 1px solid transparent;
}
#huntr-react-container-2 .ql-toolbar.ql-snow .ql-picker-options {
  border: 1px solid transparent;
  box-shadow: rgba(0,0,0,0.2) 0 2px 8px;
}
#huntr-react-container-2 .ql-toolbar.ql-snow .ql-picker.ql-expanded .ql-picker-label {
  border-color: #ccc;
}
#huntr-react-container-2 .ql-toolbar.ql-snow .ql-picker.ql-expanded .ql-picker-options {
  border-color: #ccc;
}
#huntr-react-container-2 .ql-toolbar.ql-snow .ql-color-picker .ql-picker-item.ql-selected,
#huntr-react-container-2 .ql-toolbar.ql-snow .ql-color-picker .ql-picker-item:hover {
  border-color: #000;
}
#huntr-react-container-2 .ql-toolbar.ql-snow + .ql-container.ql-snow {
  border-top: 0px;
  padding-bottom: 40px;
}
#huntr-react-container-2 .ql-snow .ql-tooltip {
  background-color: #fff;
  border: 1px solid #ccc;
  box-shadow: 0px 0px 5px #ddd;
  color: #444;
  padding: 5px 12px;
  white-space: nowrap;
}
#huntr-react-container-2 .ql-snow .ql-tooltip::before {
  content: "Visit URL:";
  line-height: 26px;
  margin-right: 8px;
}
#huntr-react-container-2 .ql-snow .ql-tooltip input[type=text] {
  display: none;
  border: 1px solid #ccc;
  font-size: 13px;
  height: 26px;
  margin: 0px;
  padding: 3px 5px;
  width: 170px;
}
#huntr-react-container-2 .ql-snow .ql-tooltip a.ql-preview {
  display: inline-block;
  max-width: 200px;
  overflow-x: hidden;
  text-overflow: ellipsis;
  vertical-align: top;
}
#huntr-react-container-2 .ql-snow .ql-tooltip a.ql-action::after {
  border-right: 1px solid #ccc;
  content: 'Edit';
  margin-left: 16px;
  padding-right: 8px;
}
#huntr-react-container-2 .ql-snow .ql-tooltip a.ql-remove::before {
  content: 'Remove';
  margin-left: 8px;
}
#huntr-react-container-2 .ql-snow .ql-tooltip a {
  line-height: 26px;
}
#huntr-react-container-2 .ql-snow .ql-tooltip.ql-editing a.ql-preview,
#huntr-react-container-2 .ql-snow .ql-tooltip.ql-editing a.ql-remove {
  display: none;
}
#huntr-react-container-2 .ql-snow .ql-tooltip.ql-editing input[type=text] {
  display: inline-block;
}
#huntr-react-container-2 .ql-snow .ql-tooltip.ql-editing a.ql-action::after {
  border-right: 0px;
  content: 'Save';
  padding-right: 0px;
}
#huntr-react-container-2 .ql-snow .ql-tooltip[data-mode=link]::before {
  content: "Enter link:";
}
#huntr-react-container-2 .ql-snow .ql-tooltip[data-mode=formula]::before {
  content: "Enter formula:";
}
#huntr-react-container-2 .ql-snow .ql-tooltip[data-mode=video]::before {
  content: "Enter video:";
}
#huntr-react-container-2 .ql-snow a {
  color: #06c;
}
</style><style type="text/css">.react-datepicker-popper[data-placement^="bottom"] .react-datepicker__triangle, .react-datepicker-popper[data-placement^="top"] .react-datepicker__triangle, .react-datepicker__year-read-view--down-arrow,
.react-datepicker__month-read-view--down-arrow,
.react-datepicker__month-year-read-view--down-arrow {
  margin-left: -8px;
  position: absolute;
}

.react-datepicker-popper[data-placement^="bottom"] .react-datepicker__triangle, .react-datepicker-popper[data-placement^="top"] .react-datepicker__triangle, .react-datepicker__year-read-view--down-arrow,
.react-datepicker__month-read-view--down-arrow,
.react-datepicker__month-year-read-view--down-arrow, .react-datepicker-popper[data-placement^="bottom"] .react-datepicker__triangle::before, .react-datepicker-popper[data-placement^="top"] .react-datepicker__triangle::before, .react-datepicker__year-read-view--down-arrow::before,
.react-datepicker__month-read-view--down-arrow::before,
.react-datepicker__month-year-read-view--down-arrow::before {
  box-sizing: content-box;
  position: absolute;
  border: 8px solid transparent;
  height: 0;
  width: 1px;
}

.react-datepicker-popper[data-placement^="bottom"] .react-datepicker__triangle::before, .react-datepicker-popper[data-placement^="top"] .react-datepicker__triangle::before, .react-datepicker__year-read-view--down-arrow::before,
.react-datepicker__month-read-view--down-arrow::before,
.react-datepicker__month-year-read-view--down-arrow::before {
  content: "";
  z-index: -1;
  border-width: 8px;
  left: -8px;
  border-bottom-color: #aeaeae;
}

.react-datepicker-popper[data-placement^="bottom"] .react-datepicker__triangle {
  top: 0;
  margin-top: -8px;
}

.react-datepicker-popper[data-placement^="bottom"] .react-datepicker__triangle, .react-datepicker-popper[data-placement^="bottom"] .react-datepicker__triangle::before {
  border-top: none;
  border-bottom-color: #f0f0f0;
}

.react-datepicker-popper[data-placement^="bottom"] .react-datepicker__triangle::before {
  top: -1px;
  border-bottom-color: #aeaeae;
}

.react-datepicker-popper[data-placement^="top"] .react-datepicker__triangle, .react-datepicker__year-read-view--down-arrow,
.react-datepicker__month-read-view--down-arrow,
.react-datepicker__month-year-read-view--down-arrow {
  bottom: 0;
  margin-bottom: -8px;
}

.react-datepicker-popper[data-placement^="top"] .react-datepicker__triangle, .react-datepicker__year-read-view--down-arrow,
.react-datepicker__month-read-view--down-arrow,
.react-datepicker__month-year-read-view--down-arrow, .react-datepicker-popper[data-placement^="top"] .react-datepicker__triangle::before, .react-datepicker__year-read-view--down-arrow::before,
.react-datepicker__month-read-view--down-arrow::before,
.react-datepicker__month-year-read-view--down-arrow::before {
  border-bottom: none;
  border-top-color: #fff;
}

.react-datepicker-popper[data-placement^="top"] .react-datepicker__triangle::before, .react-datepicker__year-read-view--down-arrow::before,
.react-datepicker__month-read-view--down-arrow::before,
.react-datepicker__month-year-read-view--down-arrow::before {
  bottom: -1px;
  border-top-color: #aeaeae;
}

.react-datepicker-wrapper {
  display: inline-block;
  padding: 0;
  border: 0;
}

.react-datepicker {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 0.8rem;
  background-color: #fff;
  color: #000;
  border: 1px solid #aeaeae;
  border-radius: 0.3rem;
  display: inline-block;
  position: relative;
}

.react-datepicker--time-only .react-datepicker__triangle {
  left: 35px;
}

.react-datepicker--time-only .react-datepicker__time-container {
  border-left: 0;
}

.react-datepicker--time-only .react-datepicker__time,
.react-datepicker--time-only .react-datepicker__time-box {
  border-bottom-left-radius: 0.3rem;
  border-bottom-right-radius: 0.3rem;
}

.react-datepicker__triangle {
  position: absolute;
  left: 50px;
}

.react-datepicker-popper {
  z-index: 1;
}

.react-datepicker-popper[data-placement^="bottom"] {
  margin-top: 10px;
}

.react-datepicker-popper[data-placement="bottom-end"] .react-datepicker__triangle, .react-datepicker-popper[data-placement="top-end"] .react-datepicker__triangle {
  left: auto;
  right: 50px;
}

.react-datepicker-popper[data-placement^="top"] {
  margin-bottom: 10px;
}

.react-datepicker-popper[data-placement^="right"] {
  margin-left: 8px;
}

.react-datepicker-popper[data-placement^="right"] .react-datepicker__triangle {
  left: auto;
  right: 42px;
}

.react-datepicker-popper[data-placement^="left"] {
  margin-right: 8px;
}

.react-datepicker-popper[data-placement^="left"] .react-datepicker__triangle {
  left: 42px;
  right: auto;
}

.react-datepicker__header {
  text-align: center;
  background-color: #f0f0f0;
  border-bottom: 1px solid #aeaeae;
  border-top-left-radius: 0.3rem;
  padding-top: 8px;
  position: relative;
}

.react-datepicker__header--time {
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

.react-datepicker__header--time:not(.react-datepicker__header--time--only) {
  border-top-left-radius: 0;
}

.react-datepicker__header:not(.react-datepicker__header--has-time-select) {
  border-top-right-radius: 0.3rem;
}

.react-datepicker__year-dropdown-container--select,
.react-datepicker__month-dropdown-container--select,
.react-datepicker__month-year-dropdown-container--select,
.react-datepicker__year-dropdown-container--scroll,
.react-datepicker__month-dropdown-container--scroll,
.react-datepicker__month-year-dropdown-container--scroll {
  display: inline-block;
  margin: 0 2px;
}

.react-datepicker__current-month,
.react-datepicker-time__header,
.react-datepicker-year-header {
  margin-top: 0;
  color: #000;
  font-weight: bold;
  font-size: 0.944rem;
}

.react-datepicker-time__header {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.react-datepicker__navigation {
  background: none;
  line-height: 1.7rem;
  text-align: center;
  cursor: pointer;
  position: absolute;
  top: 10px;
  width: 0;
  padding: 0;
  border: 0.45rem solid transparent;
  z-index: 1;
  height: 10px;
  width: 10px;
  text-indent: -999em;
  overflow: hidden;
}

.react-datepicker__navigation--previous {
  left: 10px;
  border-right-color: #ccc;
}

.react-datepicker__navigation--previous:hover {
  border-right-color: #b3b3b3;
}

.react-datepicker__navigation--previous--disabled, .react-datepicker__navigation--previous--disabled:hover {
  border-right-color: #e6e6e6;
  cursor: default;
}

.react-datepicker__navigation--next {
  right: 10px;
  border-left-color: #ccc;
}

.react-datepicker__navigation--next--with-time:not(.react-datepicker__navigation--next--with-today-button) {
  right: 95px;
}

.react-datepicker__navigation--next:hover {
  border-left-color: #b3b3b3;
}

.react-datepicker__navigation--next--disabled, .react-datepicker__navigation--next--disabled:hover {
  border-left-color: #e6e6e6;
  cursor: default;
}

.react-datepicker__navigation--years {
  position: relative;
  top: 0;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.react-datepicker__navigation--years-previous {
  top: 4px;
  border-top-color: #ccc;
}

.react-datepicker__navigation--years-previous:hover {
  border-top-color: #b3b3b3;
}

.react-datepicker__navigation--years-upcoming {
  top: -4px;
  border-bottom-color: #ccc;
}

.react-datepicker__navigation--years-upcoming:hover {
  border-bottom-color: #b3b3b3;
}

.react-datepicker__month-container {
  float: left;
}

.react-datepicker__year {
  margin: 0.4rem;
  text-align: center;
}

.react-datepicker__year-wrapper {
  display: flex;
  flex-wrap: wrap;
  max-width: 180px;
}

.react-datepicker__year .react-datepicker__year-text {
  display: inline-block;
  width: 4rem;
  margin: 2px;
}

.react-datepicker__month {
  margin: 0.4rem;
  text-align: center;
}

.react-datepicker__month .react-datepicker__month-text,
.react-datepicker__month .react-datepicker__quarter-text {
  display: inline-block;
  width: 4rem;
  margin: 2px;
}

.react-datepicker__input-time-container {
  clear: both;
  width: 100%;
  float: left;
  margin: 5px 0 10px 15px;
  text-align: left;
}

.react-datepicker__input-time-container .react-datepicker-time__caption {
  display: inline-block;
}

.react-datepicker__input-time-container .react-datepicker-time__input-container {
  display: inline-block;
}

.react-datepicker__input-time-container .react-datepicker-time__input-container .react-datepicker-time__input {
  display: inline-block;
  margin-left: 10px;
}

.react-datepicker__input-time-container .react-datepicker-time__input-container .react-datepicker-time__input input {
  width: auto;
}

.react-datepicker__input-time-container .react-datepicker-time__input-container .react-datepicker-time__input input[type="time"]::-webkit-inner-spin-button,
.react-datepicker__input-time-container .react-datepicker-time__input-container .react-datepicker-time__input input[type="time"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.react-datepicker__input-time-container .react-datepicker-time__input-container .react-datepicker-time__input input[type="time"] {
  -moz-appearance: textfield;
}

.react-datepicker__input-time-container .react-datepicker-time__input-container .react-datepicker-time__delimiter {
  margin-left: 5px;
  display: inline-block;
}

.react-datepicker__time-container {
  float: right;
  border-left: 1px solid #aeaeae;
  width: 85px;
}

.react-datepicker__time-container--with-today-button {
  display: inline;
  border: 1px solid #aeaeae;
  border-radius: 0.3rem;
  position: absolute;
  right: -72px;
  top: 0;
}

.react-datepicker__time-container .react-datepicker__time {
  position: relative;
  background: white;
  border-bottom-right-radius: 0.3rem;
}

.react-datepicker__time-container .react-datepicker__time .react-datepicker__time-box {
  width: 85px;
  overflow-x: hidden;
  margin: 0 auto;
  text-align: center;
  border-bottom-right-radius: 0.3rem;
}

.react-datepicker__time-container .react-datepicker__time .react-datepicker__time-box ul.react-datepicker__time-list {
  list-style: none;
  margin: 0;
  height: calc(195px + (1.7rem / 2));
  overflow-y: scroll;
  padding-right: 0px;
  padding-left: 0px;
  width: 100%;
  box-sizing: content-box;
}

.react-datepicker__time-container .react-datepicker__time .react-datepicker__time-box ul.react-datepicker__time-list li.react-datepicker__time-list-item {
  height: 30px;
  padding: 5px 10px;
  white-space: nowrap;
}

.react-datepicker__time-container .react-datepicker__time .react-datepicker__time-box ul.react-datepicker__time-list li.react-datepicker__time-list-item:hover {
  cursor: pointer;
  background-color: #f0f0f0;
}

.react-datepicker__time-container .react-datepicker__time .react-datepicker__time-box ul.react-datepicker__time-list li.react-datepicker__time-list-item--selected {
  background-color: #216ba5;
  color: white;
  font-weight: bold;
}

.react-datepicker__time-container .react-datepicker__time .react-datepicker__time-box ul.react-datepicker__time-list li.react-datepicker__time-list-item--selected:hover {
  background-color: #216ba5;
}

.react-datepicker__time-container .react-datepicker__time .react-datepicker__time-box ul.react-datepicker__time-list li.react-datepicker__time-list-item--disabled {
  color: #ccc;
}

.react-datepicker__time-container .react-datepicker__time .react-datepicker__time-box ul.react-datepicker__time-list li.react-datepicker__time-list-item--disabled:hover {
  cursor: default;
  background-color: transparent;
}

.react-datepicker__week-number {
  color: #ccc;
  display: inline-block;
  width: 1.7rem;
  line-height: 1.7rem;
  text-align: center;
  margin: 0.166rem;
}

.react-datepicker__week-number.react-datepicker__week-number--clickable {
  cursor: pointer;
}

.react-datepicker__week-number.react-datepicker__week-number--clickable:hover {
  border-radius: 0.3rem;
  background-color: #f0f0f0;
}

.react-datepicker__day-names,
.react-datepicker__week {
  white-space: nowrap;
}

.react-datepicker__day-name,
.react-datepicker__day,
.react-datepicker__time-name {
  color: #000;
  display: inline-block;
  width: 1.7rem;
  line-height: 1.7rem;
  text-align: center;
  margin: 0.166rem;
}

.react-datepicker__month--selected, .react-datepicker__month--in-selecting-range, .react-datepicker__month--in-range,
.react-datepicker__quarter--selected,
.react-datepicker__quarter--in-selecting-range,
.react-datepicker__quarter--in-range {
  border-radius: 0.3rem;
  background-color: #216ba5;
  color: #fff;
}

.react-datepicker__month--selected:hover, .react-datepicker__month--in-selecting-range:hover, .react-datepicker__month--in-range:hover,
.react-datepicker__quarter--selected:hover,
.react-datepicker__quarter--in-selecting-range:hover,
.react-datepicker__quarter--in-range:hover {
  background-color: #1d5d90;
}

.react-datepicker__month--disabled,
.react-datepicker__quarter--disabled {
  color: #ccc;
  pointer-events: none;
}

.react-datepicker__month--disabled:hover,
.react-datepicker__quarter--disabled:hover {
  cursor: default;
  background-color: transparent;
}

.react-datepicker__day,
.react-datepicker__month-text,
.react-datepicker__quarter-text,
.react-datepicker__year-text {
  cursor: pointer;
}

.react-datepicker__day:hover,
.react-datepicker__month-text:hover,
.react-datepicker__quarter-text:hover,
.react-datepicker__year-text:hover {
  border-radius: 0.3rem;
  background-color: #f0f0f0;
}

.react-datepicker__day--today,
.react-datepicker__month-text--today,
.react-datepicker__quarter-text--today,
.react-datepicker__year-text--today {
  font-weight: bold;
}

.react-datepicker__day--highlighted,
.react-datepicker__month-text--highlighted,
.react-datepicker__quarter-text--highlighted,
.react-datepicker__year-text--highlighted {
  border-radius: 0.3rem;
  background-color: #3dcc4a;
  color: #fff;
}

.react-datepicker__day--highlighted:hover,
.react-datepicker__month-text--highlighted:hover,
.react-datepicker__quarter-text--highlighted:hover,
.react-datepicker__year-text--highlighted:hover {
  background-color: #32be3f;
}

.react-datepicker__day--highlighted-custom-1,
.react-datepicker__month-text--highlighted-custom-1,
.react-datepicker__quarter-text--highlighted-custom-1,
.react-datepicker__year-text--highlighted-custom-1 {
  color: magenta;
}

.react-datepicker__day--highlighted-custom-2,
.react-datepicker__month-text--highlighted-custom-2,
.react-datepicker__quarter-text--highlighted-custom-2,
.react-datepicker__year-text--highlighted-custom-2 {
  color: green;
}

.react-datepicker__day--selected, .react-datepicker__day--in-selecting-range, .react-datepicker__day--in-range,
.react-datepicker__month-text--selected,
.react-datepicker__month-text--in-selecting-range,
.react-datepicker__month-text--in-range,
.react-datepicker__quarter-text--selected,
.react-datepicker__quarter-text--in-selecting-range,
.react-datepicker__quarter-text--in-range,
.react-datepicker__year-text--selected,
.react-datepicker__year-text--in-selecting-range,
.react-datepicker__year-text--in-range {
  border-radius: 0.3rem;
  background-color: #216ba5;
  color: #fff;
}

.react-datepicker__day--selected:hover, .react-datepicker__day--in-selecting-range:hover, .react-datepicker__day--in-range:hover,
.react-datepicker__month-text--selected:hover,
.react-datepicker__month-text--in-selecting-range:hover,
.react-datepicker__month-text--in-range:hover,
.react-datepicker__quarter-text--selected:hover,
.react-datepicker__quarter-text--in-selecting-range:hover,
.react-datepicker__quarter-text--in-range:hover,
.react-datepicker__year-text--selected:hover,
.react-datepicker__year-text--in-selecting-range:hover,
.react-datepicker__year-text--in-range:hover {
  background-color: #1d5d90;
}

.react-datepicker__day--keyboard-selected,
.react-datepicker__month-text--keyboard-selected,
.react-datepicker__quarter-text--keyboard-selected,
.react-datepicker__year-text--keyboard-selected {
  border-radius: 0.3rem;
  background-color: #2a87d0;
  color: #fff;
}

.react-datepicker__day--keyboard-selected:hover,
.react-datepicker__month-text--keyboard-selected:hover,
.react-datepicker__quarter-text--keyboard-selected:hover,
.react-datepicker__year-text--keyboard-selected:hover {
  background-color: #1d5d90;
}

.react-datepicker__day--in-selecting-range ,
.react-datepicker__month-text--in-selecting-range ,
.react-datepicker__quarter-text--in-selecting-range ,
.react-datepicker__year-text--in-selecting-range {
  background-color: rgba(33, 107, 165, 0.5);
}

.react-datepicker__month--selecting-range .react-datepicker__day--in-range , .react-datepicker__month--selecting-range
.react-datepicker__month-text--in-range , .react-datepicker__month--selecting-range
.react-datepicker__quarter-text--in-range , .react-datepicker__month--selecting-range
.react-datepicker__year-text--in-range {
  background-color: #f0f0f0;
  color: #000;
}

.react-datepicker__day--disabled,
.react-datepicker__month-text--disabled,
.react-datepicker__quarter-text--disabled,
.react-datepicker__year-text--disabled {
  cursor: default;
  color: #ccc;
}

.react-datepicker__day--disabled:hover,
.react-datepicker__month-text--disabled:hover,
.react-datepicker__quarter-text--disabled:hover,
.react-datepicker__year-text--disabled:hover {
  background-color: transparent;
}

.react-datepicker__month-text.react-datepicker__month--selected:hover, .react-datepicker__month-text.react-datepicker__month--in-range:hover, .react-datepicker__month-text.react-datepicker__quarter--selected:hover, .react-datepicker__month-text.react-datepicker__quarter--in-range:hover,
.react-datepicker__quarter-text.react-datepicker__month--selected:hover,
.react-datepicker__quarter-text.react-datepicker__month--in-range:hover,
.react-datepicker__quarter-text.react-datepicker__quarter--selected:hover,
.react-datepicker__quarter-text.react-datepicker__quarter--in-range:hover {
  background-color: #216ba5;
}

.react-datepicker__month-text:hover,
.react-datepicker__quarter-text:hover {
  background-color: #f0f0f0;
}

.react-datepicker__input-container {
  position: relative;
  display: inline-block;
  width: 100%;
}

.react-datepicker__year-read-view,
.react-datepicker__month-read-view,
.react-datepicker__month-year-read-view {
  border: 1px solid transparent;
  border-radius: 0.3rem;
}

.react-datepicker__year-read-view:hover,
.react-datepicker__month-read-view:hover,
.react-datepicker__month-year-read-view:hover {
  cursor: pointer;
}

.react-datepicker__year-read-view:hover .react-datepicker__year-read-view--down-arrow,
.react-datepicker__year-read-view:hover .react-datepicker__month-read-view--down-arrow,
.react-datepicker__month-read-view:hover .react-datepicker__year-read-view--down-arrow,
.react-datepicker__month-read-view:hover .react-datepicker__month-read-view--down-arrow,
.react-datepicker__month-year-read-view:hover .react-datepicker__year-read-view--down-arrow,
.react-datepicker__month-year-read-view:hover .react-datepicker__month-read-view--down-arrow {
  border-top-color: #b3b3b3;
}

.react-datepicker__year-read-view--down-arrow,
.react-datepicker__month-read-view--down-arrow,
.react-datepicker__month-year-read-view--down-arrow {
  border-top-color: #ccc;
  float: right;
  margin-left: 20px;
  top: 8px;
  position: relative;
  border-width: 0.45rem;
}

.react-datepicker__year-dropdown,
.react-datepicker__month-dropdown,
.react-datepicker__month-year-dropdown {
  background-color: #f0f0f0;
  position: absolute;
  width: 50%;
  left: 25%;
  top: 30px;
  z-index: 1;
  text-align: center;
  border-radius: 0.3rem;
  border: 1px solid #aeaeae;
}

.react-datepicker__year-dropdown:hover,
.react-datepicker__month-dropdown:hover,
.react-datepicker__month-year-dropdown:hover {
  cursor: pointer;
}

.react-datepicker__year-dropdown--scrollable,
.react-datepicker__month-dropdown--scrollable,
.react-datepicker__month-year-dropdown--scrollable {
  height: 150px;
  overflow-y: scroll;
}

.react-datepicker__year-option,
.react-datepicker__month-option,
.react-datepicker__month-year-option {
  line-height: 20px;
  width: 100%;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.react-datepicker__year-option:first-of-type,
.react-datepicker__month-option:first-of-type,
.react-datepicker__month-year-option:first-of-type {
  border-top-left-radius: 0.3rem;
  border-top-right-radius: 0.3rem;
}

.react-datepicker__year-option:last-of-type,
.react-datepicker__month-option:last-of-type,
.react-datepicker__month-year-option:last-of-type {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  border-bottom-left-radius: 0.3rem;
  border-bottom-right-radius: 0.3rem;
}

.react-datepicker__year-option:hover,
.react-datepicker__month-option:hover,
.react-datepicker__month-year-option:hover {
  background-color: #ccc;
}

.react-datepicker__year-option:hover .react-datepicker__navigation--years-upcoming,
.react-datepicker__month-option:hover .react-datepicker__navigation--years-upcoming,
.react-datepicker__month-year-option:hover .react-datepicker__navigation--years-upcoming {
  border-bottom-color: #b3b3b3;
}

.react-datepicker__year-option:hover .react-datepicker__navigation--years-previous,
.react-datepicker__month-option:hover .react-datepicker__navigation--years-previous,
.react-datepicker__month-year-option:hover .react-datepicker__navigation--years-previous {
  border-top-color: #b3b3b3;
}

.react-datepicker__year-option--selected,
.react-datepicker__month-option--selected,
.react-datepicker__month-year-option--selected {
  position: absolute;
  left: 15px;
}

.react-datepicker__close-icon {
  cursor: pointer;
  background-color: transparent;
  border: 0;
  outline: 0;
  padding: 0px 6px 0px 0px;
  position: absolute;
  top: 0;
  right: 0;
  height: 100%;
  display: table-cell;
  vertical-align: middle;
}

.react-datepicker__close-icon::after {
  cursor: pointer;
  background-color: #216ba5;
  color: #fff;
  border-radius: 50%;
  height: 16px;
  width: 16px;
  padding: 2px;
  font-size: 12px;
  line-height: 1;
  text-align: center;
  display: table-cell;
  vertical-align: middle;
  content: "\D7";
}

.react-datepicker__today-button {
  background: #f0f0f0;
  border-top: 1px solid #aeaeae;
  cursor: pointer;
  text-align: center;
  font-weight: bold;
  padding: 5px 0;
  clear: left;
}

.react-datepicker__portal {
  position: fixed;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.8);
  left: 0;
  top: 0;
  justify-content: center;
  align-items: center;
  display: flex;
  z-index: 2147483647;
}

.react-datepicker__portal .react-datepicker__day-name,
.react-datepicker__portal .react-datepicker__day,
.react-datepicker__portal .react-datepicker__time-name {
  width: 3rem;
  line-height: 3rem;
}

@media (max-width: 400px), (max-height: 550px) {
  .react-datepicker__portal .react-datepicker__day-name,
  .react-datepicker__portal .react-datepicker__day,
  .react-datepicker__portal .react-datepicker__time-name {
    width: 2rem;
    line-height: 2rem;
  }
}

.react-datepicker__portal .react-datepicker__current-month,
.react-datepicker__portal .react-datepicker-time__header {
  font-size: 1.44rem;
}

.react-datepicker__portal .react-datepicker__navigation {
  border: 0.81rem solid transparent;
}

.react-datepicker__portal .react-datepicker__navigation--previous {
  border-right-color: #ccc;
}

.react-datepicker__portal .react-datepicker__navigation--previous:hover {
  border-right-color: #b3b3b3;
}

.react-datepicker__portal .react-datepicker__navigation--previous--disabled, .react-datepicker__portal .react-datepicker__navigation--previous--disabled:hover {
  border-right-color: #e6e6e6;
  cursor: default;
}

.react-datepicker__portal .react-datepicker__navigation--next {
  border-left-color: #ccc;
}

.react-datepicker__portal .react-datepicker__navigation--next:hover {
  border-left-color: #b3b3b3;
}

.react-datepicker__portal .react-datepicker__navigation--next--disabled, .react-datepicker__portal .react-datepicker__navigation--next--disabled:hover {
  border-left-color: #e6e6e6;
  cursor: default;
}
</style><style type="text/css">@font-face { font-family: 'simple-line-icons'; src: url('chrome-extension://mihdfbecejheednfigjpdacgeilhlmnf/assets/fonts/Simple-Line-Icons.ttf') format('truetype'); }</style><script type="application/javascript" src="./DataReader_files/codespaces-3edb28db.js.download"></script><script type="application/javascript" src="./DataReader_files/topic-suggestions-55d0e74f.js.download"></script><meta name="selected-link" value="repo_source" data-pjax-transient=""><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient=""><meta name="request-id" content="BA50:773C:124157D:13B0D83:60BE7F82" data-pjax-transient=""><meta name="html-safe-nonce" content="6a4c8056cfc0e0a65cf323698a706b6757bc546d5ce40ad1cb60a676617d0629" data-pjax-transient=""><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9aZXlhZFphbmF0eS9pbWFnZS1jbHVzdGVyaW5nL2Jsb2IvbWFzdGVyL0RhdGFSZWFkZXIucHkiLCJyZXF1ZXN0X2lkIjoiQkE1MDo3NzNDOjEyNDE1N0Q6MTNCMEQ4Mzo2MEJFN0Y4MiIsInZpc2l0b3JfaWQiOiI2OTE4MzExMDM5NzI5NTQ5MjIzIiwicmVnaW9uX2VkZ2UiOiJhcC1zb3V0aC0xIiwicmVnaW9uX3JlbmRlciI6ImlhZCJ9" data-pjax-transient=""><meta name="visitor-hmac" content="65764356a6fb358b5945e0c7f0559e1adfe33e8fee219d37a8a2ddc322055ad8" data-pjax-transient=""><meta name="github-keyboard-shortcuts" content="repository,source-code" data-pjax-transient=""><meta name="hovercard-subject-tag" content="repository:161846877" data-pjax-transient=""><link rel="canonical" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py" data-pjax-transient=""></head>

  <body class="logged-out env-production page-responsive page-blob intent-mouse" style="word-wrap: break-word;" data-new-gr-c-s-loaded="14.1014.0">
    

    <div class="position-relative js-header-wrapper ">
      <a href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py#start-of-content" class="px-2 py-4 color-bg-info-inverse color-text-white show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader width-full js-pjax-loader-bar Progress position-fixed">
    <span style="background-color: rgb(121, 184, 255); width: 100%; transition: width 0.4s ease 0s;" data-view-component="true" class="Progress-item progress-pjax-loader-bar"></span>
</span>      
      


        
            <header class="Header-old header-logged-out js-details-container Details position-relative f4 py-2" role="banner">
  <div class="container-xl d-lg-flex flex-items-center p-responsive">
    <div class="d-flex flex-justify-between flex-items-center">
        <a class="mr-4" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
          <svg height="32" class="octicon octicon-mark-github color-text-white" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
        </a>

          <div class="d-lg-none css-truncate css-truncate-target width-fit p-2">
            

          </div>

        <div class="d-flex flex-items-center">
              <nux-signup-candidates data-attribute-name="href" data-candidate-url="/join_next?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fblob%2Fshow&amp;source=header-repo" data-action="loaded:nux-signup-candidates#determineSignupAction" data-catalyst="" data-form-method="">
                <a href="https://github.com/join?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fblob%2Fshow&amp;source=header-repo" class="d-inline-block d-lg-none f5 color-text-white no-underline border color-border-tertiary rounded-2 px-2 py-1 mr-3 mr-sm-5" data-target="nux-signup-candidates.signupAction" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/cifar_image_clustering.ipynb&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="334a6456c497a57bb5b9104f0991b0e769f1044a1717364633a9dcdf2374b8ab">
                  Sign&nbsp;up
                </a>
              </nux-signup-candidates>

          <button class="btn-link d-lg-none mt-1 js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
            <svg height="24" class="octicon octicon-three-bars color-text-white" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z"></path></svg>
          </button>
        </div>
    </div>

    <div class="HeaderMenu HeaderMenu--logged-out position-fixed top-0 right-0 bottom-0 height-fit position-lg-relative d-lg-flex flex-justify-between flex-items-center flex-auto">
      <div class="d-flex d-lg-none flex-justify-end border-bottom color-bg-secondary p-3">
        <button class="btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
          <svg height="24" class="octicon octicon-x color-text-secondary" viewBox="0 0 24 24" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M5.72 5.72a.75.75 0 011.06 0L12 10.94l5.22-5.22a.75.75 0 111.06 1.06L13.06 12l5.22 5.22a.75.75 0 11-1.06 1.06L12 13.06l-5.22 5.22a.75.75 0 01-1.06-1.06L10.94 12 5.72 6.78a.75.75 0 010-1.06z"></path></svg>
        </button>
      </div>

        <nav class="mt-0 px-3 px-lg-0 mb-5 mb-lg-0" aria-label="Global">
          <ul class="d-lg-flex list-style-none">
              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Why GitHub?
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>
                  <div class="dropdown-menu flex-auto rounded px-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <a href="https://github.com/features" class="py-2 lh-condensed-ultra d-block Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features">Features <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a>
                    <ul class="list-style-none f5 pb-3">
                        <li class="edge-item-fix"><a href="https://github.com/mobile" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Mobile <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                        <li class="edge-item-fix"><a href="https://github.com/features/actions" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Actions <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                        <li class="edge-item-fix"><a href="https://github.com/features/codespaces" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Codespaces <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                        <li class="edge-item-fix"><a href="https://github.com/features/packages" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Packages <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                        <li class="edge-item-fix"><a href="https://github.com/features/security" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Security <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                        <li class="edge-item-fix"><a href="https://github.com/features/code-review/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Code review <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                        <li class="edge-item-fix"><a href="https://github.com/features/project-management/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Project management <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                        <li class="edge-item-fix"><a href="https://github.com/features/integrations" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Integrations <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="https://github.com/sponsors" class="py-2 lh-condensed-ultra d-block no-underline Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Sponsors">GitHub Sponsors <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://github.com/customer-stories" class="py-2 lh-condensed-ultra d-block no-underline Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Customer stories">Customer stories<span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="https://github.com/team" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Team">Team</a>
              </li>
              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="https://github.com/enterprise" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Enterprise">Enterprise</a>
              </li>

              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Explore
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded px-0 pt-2 pb-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="https://github.com/explore" class="py-2 lh-condensed-ultra d-block Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Explore">Explore GitHub <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>

                    <h4 class="color-text-tertiary text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Learn and contribute</h4>
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="https://github.com/topics" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Topics">Topics <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                        <li class="edge-item-fix"><a href="https://github.com/collections" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Collections">Collections <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://github.com/trending" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Trending">Trending <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://lab.github.com/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Learning lab">Learning Lab <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://opensource.guide/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Open source guides">Open source guides <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>

                    <h4 class="color-text-tertiary text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Connect with others</h4>
                    <ul class="list-style-none mb-0">
                      <li class="edge-item-fix"><a href="https://github.com/readme" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">The ReadME Project <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://github.com/events" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Events">Events <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://github.community/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Community forum">Community forum <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to GitHub Education">GitHub Education <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://stars.github.com/" class="py-2 pb-0 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to GitHub Stars Program">GitHub Stars program <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>

              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="https://github.com/marketplace" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace">Marketplace</a>
              </li>

              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Pricing
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                       <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded px-0 pt-2 pb-4 mt-0 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <a href="https://github.com/pricing" class="pb-2 lh-condensed-ultra d-block Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing">Plans <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a>

                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="https://github.com/pricing#feature-comparison" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Compare plans">Compare plans <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://enterprise.github.com/contact" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Contact Sales">Contact Sales <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="https://education.github.com/" class="py-2 pb-0 lh-condensed-ultra d-block no-underline Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Education">Education <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
          </ul>
        </nav>

      <div class="d-lg-flex flex-items-center px-3 px-lg-0 text-center text-lg-left">
          <div class="d-lg-flex min-width-0 mb-3 mb-lg-0">
            


  <div class="header-search flex-auto js-site-search position-relative flex-self-stretch flex-md-self-auto mb-3 mb-md-0 mr-0 mr-md-3 scoped-search site-scoped-search js-jump-to">
    <div class="position-relative">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="161846877" data-scoped-search-url="/ZeyadZanaty/image-clustering/search" data-owner-scoped-search-url="/users/ZeyadZanaty/search" data-unscoped-search-url="/search" action="https://github.com/ZeyadZanaty/image-clustering/search" accept-charset="UTF-8" method="get">
        <label class="form-control input-sm header-search-wrapper p-0 js-chromeless-input-container header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center">
          <input type="text" class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable" data-hotkey="s,/" name="q" value="" placeholder="Search" data-unscoped-placeholder="Search GitHub" data-scoped-placeholder="Search" autocapitalize="off" role="combobox" aria-haspopup="listbox" aria-expanded="false" aria-autocomplete="list" aria-controls="jump-to-results" aria-label="Search" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" spellcheck="false" autocomplete="off">
          <input type="hidden" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" value="ebDgB5U1WMXNK/l+UWvBhuT7Mje11iMTFcZp99MxXnlOASmErnYUFrYd9vJZ3Qmg9wfbo/1SteKkesHwuERb1g==">
          <input type="hidden" class="js-site-search-type-field" name="type">
              <img src="./DataReader_files/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py" data-item-type="suggestion">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="color-text-secondary">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py" data-item-type="scoped_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-owner-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py" data-item-type="owner_scoped_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this user">
        In this user
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py" data-item-type="global_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


</ul>

            </div>
        </label>
</form>    </div>
  </div>

          </div>

        <a href="https://github.com/login?return_to=%2FZeyadZanaty%2Fimage-clustering%2Fblob%2Fmaster%2Fcifar_image_clustering.ipynb" class="HeaderMenu-link flex-shrink-0 no-underline mr-3" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/cifar_image_clustering.ipynb&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ca11841f79ea807739755d7377f7f4f32b7c9b9b74b921927c63752dd5a4611e" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">
          Sign in
        </a>
            <nux-signup-candidates data-attribute-name="href" data-candidate-url="/join_next?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fblob%2Fshow&amp;source=header-repo&amp;source_repo=ZeyadZanaty%2Fimage-clustering" data-action="loaded:nux-signup-candidates#determineSignupAction" data-catalyst="" data-form-method="">
              <a href="https://github.com/join?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fblob%2Fshow&amp;source=header-repo&amp;source_repo=ZeyadZanaty%2Fimage-clustering" class="HeaderMenu-link flex-shrink-0 d-inline-block no-underline border color-border-tertiary rounded px-2 py-1" data-target="nux-signup-candidates.signupAction" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/cifar_image_clustering.ipynb&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ca11841f79ea807739755d7377f7f4f32b7c9b9b74b921927c63752dd5a4611e">
                Sign up
              </a>
            </nux-signup-candidates>
      </div>
    </div>
  </div>
</header>

    </div>

  <div id="start-of-content" class="show-on-focus"></div>





    <div data-pjax-replace="" id="js-flash-container">


  <template class="js-flash-template"></template>
</div>


    

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>




  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" data-pjax-container="">


      




  


  <div class="color-bg-secondary pt-3 hide-full-screen mb-5">

      <div class="d-flex mb-3 px-3 px-md-4 px-lg-5">

        <div class="flex-auto min-width-0 width-fit mr-3">
            <h1 class=" d-flex flex-wrap flex-items-center break-word f3 text-normal">
    <svg class="octicon octicon-repo color-text-secondary mr-2" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
  <span class="author flex-self-stretch" itemprop="author">
    <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/ZeyadZanaty/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ZeyadZanaty">ZeyadZanaty</a>
  </span>
  <span class="mx-1 flex-self-stretch color-text-secondary">/</span>
  <strong itemprop="name" class="mr-2 flex-self-stretch">
    <a data-pjax="#js-repo-pjax-container" href="https://github.com/ZeyadZanaty/image-clustering">image-clustering</a>
  </strong>
  
</h1>


        </div>

          <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">

  <li>
        <notifications-list-subscription-form class="f5 position-relative d-flex" data-catalyst="">
      <details class="details-reset details-overlay f5 position-relative" data-target="notifications-list-subscription-form.details" data-action="toggle:notifications-list-subscription-form#detailsToggled">

      <summary class="btn btn-sm rounded-right-0" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:161846877,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering?_pjax=%23js-repo-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="66034410dadb6026955c76c51c03528351c44c1ee7a8a228965b13108a2865f5" data-ga-click="Repository, click Watch settings, action:files#disambiguate" aria-label="Notifications settings" aria-haspopup="menu" role="button">
          <span data-menu-button="">
            <span hidden="" data-target="notifications-list-subscription-form.unwatchButtonCopy">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-eye">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
              Unwatch
            </span>
            <span hidden="" data-target="notifications-list-subscription-form.stopIgnoringButtonCopy">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-bell-slash">
    <path fill-rule="evenodd" d="M8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 014.38 1.55 5 5 0 0113 5v2.373a.75.75 0 01-1.5 0V5A3.5 3.5 0 008 1.5zM4.182 4.31L1.19 2.143a.75.75 0 10-.88 1.214L3 5.305v2.642a.25.25 0 01-.042.139L1.255 10.64A1.518 1.518 0 002.518 13h11.108l1.184.857a.75.75 0 10.88-1.214l-1.375-.996a1.196 1.196 0 00-.013-.01L4.198 4.321a.733.733 0 00-.016-.011zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01.015.015 0 00.005.012.017.017 0 00.006.004l.007.001h9.037zM8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path>
</svg>
              Stop ignoring
            </span>
            <span data-target="notifications-list-subscription-form.watchButtonCopy">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-eye">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
              Watch
            </span>
          </span>
          <span class="dropdown-caret"></span>
</summary>
        <details-menu class="SelectMenu  " role="menu" data-target="notifications-list-subscription-form.menu">
          <div class="SelectMenu-modal notifications-component-menu-modal">
            <header class="SelectMenu-header">
              <h3 class="SelectMenu-title">Notifications</h3>
              <button class="SelectMenu-closeButton" type="button" aria-label="Close menu" data-action="click:notifications-list-subscription-form#closeMenu">
                <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
              </button>
            </header>

            <div class="SelectMenu-list">
              <form data-target="notifications-list-subscription-form.form" data-action="submit:notifications-list-subscription-form#submitForm" action="https://github.com/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="ovu/w1VUow0yC5g2PD3aqn10c7W5YTi8PEX7XZtlJrnwsH/H1Ao5UmLBcyLbb0zsFKUmVRkqdt6xUq5skxlmGw==">

                <input type="hidden" name="repository_id" value="161846877">

                <button type="submit" name="do" value="included" class="SelectMenu-item flex-items-start" role="menuitemradio" aria-checked="true" data-targets="notifications-list-subscription-form.subscriptionButtons">
                  <span class="f5">
                    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      Participating and @mentions
                    </div>
                    <div class="text-small color-text-secondary text-normal pb-1">
                      Only receive notifications from this repository when participating or @mentioned.
                    </div>
                  </div>
                </button>

                <button type="submit" name="do" value="subscribed" class="SelectMenu-item flex-items-start" role="menuitemradio" aria-checked="false" data-targets="notifications-list-subscription-form.subscriptionButtons">
                  <span class="f5">
                    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      All Activity
                    </div>
                    <div class="text-small color-text-secondary text-normal pb-1">
                      Notified of all notifications on this repository.
                    </div>
                  </div>
                </button>

                <button type="submit" name="do" value="ignore" class="SelectMenu-item flex-items-start" role="menuitemradio" aria-checked="false" data-targets="notifications-list-subscription-form.subscriptionButtons">
                  <span class="f5">
                    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      Ignore
                    </div>
                    <div class="text-small color-text-secondary text-normal pb-1">
                      Never be notified.
                    </div>
                  </div>
                </button>
</form>
              <button class="SelectMenu-item flex-items-start pr-3" type="button" role="menuitemradio" data-target="notifications-list-subscription-form.customButton" data-action="click:notifications-list-subscription-form#openCustomDialog" aria-haspopup="true" aria-checked="false">
                <span class="f5">
                  <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                </span>
                <div>
                  <div class="d-flex flex-items-start flex-justify-between">
                    <div class="f5 text-bold">Custom</div>
                    <div class="f5 pr-1">
                      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-arrow-right">
    <path fill-rule="evenodd" d="M8.22 2.97a.75.75 0 011.06 0l4.25 4.25a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06-1.06l2.97-2.97H3.75a.75.75 0 010-1.5h7.44L8.22 4.03a.75.75 0 010-1.06z"></path>
</svg>
                    </div>
                  </div>
                  <div class="text-small color-text-secondary text-normal pb-1">
                    Select events you want to be notified of in addition to participating and @mentions.
                  </div>
                </div>
              </button>
            </div>
          </div>
        </details-menu>

        <details-dialog class="notifications-component-dialog " data-target="notifications-list-subscription-form.customDialog" hidden="" role="dialog" aria-modal="true">
          <div class="SelectMenu-modal notifications-component-dialog-modal overflow-visible">
            <form data-target="notifications-list-subscription-form.customform" data-action="submit:notifications-list-subscription-form#submitCustomForm" action="https://github.com/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="mLQApw1GfB8xIF/Jc5SEhxqVDRXY4wAhChHqexrNT27K/8CjjBjmQGHqtN2UxhLBc0RY9XioTkOHBr9KErEPzA==">

              <input type="hidden" name="repository_id" value="161846877">

              <header class="d-sm-none SelectMenu-header pb-0 border-bottom-0 px-2 px-sm-3">
                <h1 class="f3 SelectMenu-title d-inline-flex">
                  <button class="color-bg-primary border-0 px-2 py-0 m-0 Link--secondary f5" aria-label="Return to menu" type="button" data-action="click:notifications-list-subscription-form#closeCustomDialog">
                    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-arrow-left">
    <path fill-rule="evenodd" d="M7.78 12.53a.75.75 0 01-1.06 0L2.47 8.28a.75.75 0 010-1.06l4.25-4.25a.75.75 0 011.06 1.06L4.81 7h7.44a.75.75 0 010 1.5H4.81l2.97 2.97a.75.75 0 010 1.06z"></path>
</svg>
                  </button>
                  Custom
                </h1>
              </header>

              <header class="d-none d-sm-flex flex-items-start pt-1">
                <button class="border-0 px-2 pt-1 m-0 Link--secondary f5" style="background-color: transparent;" aria-label="Return to menu" type="button" data-action="click:notifications-list-subscription-form#closeCustomDialog">
                  <svg style="position: relative; left: 2px; top: 1px" aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-arrow-left">
    <path fill-rule="evenodd" d="M7.78 12.53a.75.75 0 01-1.06 0L2.47 8.28a.75.75 0 010-1.06l4.25-4.25a.75.75 0 011.06 1.06L4.81 7h7.44a.75.75 0 010 1.5H4.81l2.97 2.97a.75.75 0 010 1.06z"></path>
</svg>
                </button>

                <h1 class="pt-1 pr-4 pb-0 pl-0 f5 text-bold">
                  Custom
                </h1>
              </header>

              <fieldset>
                <legend>
                  <div class="text-small color-text-secondary pt-0 pr-3 pb-3 pl-6 pl-sm-5 border-bottom mb-3">
                    Select events you want to be notified of in addition to participating and @mentions.
                  </div>
                </legend>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="Issue" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Issues
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="PullRequest" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Pull requests
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="Release" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Releases
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="Discussion" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Discussions
                    </label>

                      <span class="tooltipped tooltipped-nw mr-2 p-1 float-right" aria-label="Discussions are not enabled for this repo">
                        <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-info color-icon-secondary">
    <path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm6.5-.25A.75.75 0 017.25 7h1a.75.75 0 01.75.75v2.75h.25a.75.75 0 010 1.5h-2a.75.75 0 010-1.5h.25v-2h-.25a.75.75 0 01-.75-.75zM8 6a1 1 0 100-2 1 1 0 000 2z"></path>
</svg>
                      </span>
                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="SecurityAlert" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Security alerts
                    </label>

                  </div>
              </fieldset>
              <div class="pt-2 pb-3 px-3 d-flex flex-justify-start flex-row-reverse">
                <button type="submit" name="do" value="custom" class="btn btn-sm btn-primary ml-2" data-target="notifications-list-subscription-form.customSubmit" disabled="">Apply</button>

                <button class="btn btn-sm" type="button" data-action="click:notifications-list-subscription-form#resetForm" data-close-dialog="">Cancel</button>
              </div>
</form>          </div>
        </details-dialog>
        <div class="notifications-component-dialog-overlay"></div>
      </details>
        <a class="social-count" href="https://github.com/ZeyadZanaty/image-clustering/watchers" aria-label="1 user is watching this repository" data-target="notifications-list-subscription-form.socialCount">
          1
        </a>
    </notifications-list-subscription-form>



  </li>

  <li>
        <div class="d-block js-toggler-container js-social-container starring-container ">
    <form class="starred js-social-form" action="https://github.com/ZeyadZanaty/image-clustering/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="c9Y+T6ROnTfrH9HzmibGJUaiKpwpkdNGfnD5zXLxOR3s1R+yLUO/g9fiD4w/K6strxujlpjAyM+eaRqVdD4etA==">
      <input type="hidden" name="context" value="repository">
      <button type="submit" class="btn btn-sm btn-with-count  js-toggler-target" aria-label="Unstar this repository" title="Unstar ZeyadZanaty/image-clustering" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:161846877,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering?_pjax=%23js-repo-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="67f5313e251cab2e2b56072d768633e7e73ff9c837fd61ecabba19ec37c6cc47" data-ga-click="Repository, click unstar button, action:files#disambiguate; text:Unstar">        <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-star-fill mr-1">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"></path>
</svg>
        <span data-view-component="true">
          Unstar
</span></button>        <a class="social-count js-social-count" href="https://github.com/ZeyadZanaty/image-clustering/stargazers" aria-label="4 users starred this repository">
           4
        </a>
</form>
    <form class="unstarred js-social-form" action="https://github.com/ZeyadZanaty/image-clustering/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="9O4bjAAJJ01jmXKH81o7/cExHT1zbV6IQ+fc1OoJ7it3Xh/6xLTQRXu+f8M5YtE6Zy/B5Kqp/S7NMapqYDh66w==">
      <input type="hidden" name="context" value="repository">
      <button type="submit" class="btn btn-sm btn-with-count  js-toggler-target" aria-label="Unstar this repository" title="Star ZeyadZanaty/image-clustering" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:161846877,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering?_pjax=%23js-repo-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="9ed641f5374a03389343c9d3d0a5bdd89f945cd7cdd57ec5c086dea79a889e51" data-ga-click="Repository, click star button, action:files#disambiguate; text:Star">        <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-star mr-1">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg>
        <span data-view-component="true">
          Star
</span></button>        <a class="social-count js-social-count" href="https://github.com/ZeyadZanaty/image-clustering/stargazers" aria-label="4 users starred this repository">
          4
        </a>
</form>  </div>

  </li>

  <li>
            <!-- '"` --><!-- </textarea></xmp> --><form class="btn-with-count" action="https://github.com/ZeyadZanaty/image-clustering/fork" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="1Kh2rd9vTdAFiOS42kYdOfi4Ta6ojQXdO7t/Y07l/DvWVZrpoa/rx0EuXCyxK5f+WILM9FfmGTlRrmwix6SMVA==">
              <button class="btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:161846877,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering?_pjax=%23js-repo-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="3188ac5e1ec32aeabdb7ff9a295d7b6498c1ea62d31f853e9b64b3e9978a8e09" data-ga-click="Repository, show fork modal, action:files#disambiguate; text:Fork" type="submit" title="Fork your own copy of ZeyadZanaty/image-clustering to your account" aria-label="Fork your own copy of ZeyadZanaty/image-clustering to your account">                <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-repo-forked">
    <path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
</svg>
                Fork
</button></form>
      <a href="https://github.com/ZeyadZanaty/image-clustering/network/members" class="social-count" aria-label="1 user forked this repository">
        1
      </a>
  </li>
</ul>

      </div>
          <div class="d-block d-md-none mb-2 px-3 px-md-4 px-lg-5">
      <p class="f4 mb-3">
        K-Means Clustering Implementation on CIFAR-10/CIFAR-100/MNIST Datasets
      </p>
      <div class="mb-2">
        <a href="https://github.com/ZeyadZanaty/image-clustering/blob/master/LICENSE" class="Link--muted">
          <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-law mr-1">
    <path fill-rule="evenodd" d="M8.75.75a.75.75 0 00-1.5 0V2h-.984c-.305 0-.604.08-.869.23l-1.288.737A.25.25 0 013.984 3H1.75a.75.75 0 000 1.5h.428L.066 9.192a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.514 3.514 0 00.686.45A4.492 4.492 0 003 11c.88 0 1.556-.22 2.023-.454a3.515 3.515 0 00.686-.45l.045-.04.016-.015.006-.006.002-.002.001-.002L5.25 9.5l.53.53a.75.75 0 00.154-.838L3.822 4.5h.162c.305 0 .604-.08.869-.23l1.289-.737a.25.25 0 01.124-.033h.984V13h-2.5a.75.75 0 000 1.5h6.5a.75.75 0 000-1.5h-2.5V3.5h.984a.25.25 0 01.124.033l1.29.736c.264.152.563.231.868.231h.162l-2.112 4.692a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.517 3.517 0 00.686.45A4.492 4.492 0 0013 11c.88 0 1.556-.22 2.023-.454a3.512 3.512 0 00.686-.45l.045-.04.01-.01.006-.005.006-.006.002-.002.001-.002-.529-.531.53.53a.75.75 0 00.154-.838L13.823 4.5h.427a.75.75 0 000-1.5h-2.234a.25.25 0 01-.124-.033l-1.29-.736A1.75 1.75 0 009.735 2H8.75V.75zM1.695 9.227c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327l-1.305 2.9zm10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327l-1.305 2.9z"></path>
</svg>
            MIT License
        </a>
      </div>
    <div class="mb-3">
      <a class="Link--secondary no-underline mr-3" href="https://github.com/ZeyadZanaty/image-clustering/stargazers">
        <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-star mr-1">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg>
        <span class="text-bold">4</span>
        stars
</a>      <a class="Link--secondary no-underline" href="https://github.com/ZeyadZanaty/image-clustering/network/members">
        <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-repo-forked mr-1">
    <path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
</svg>
        <span class="text-bold">1</span>
        fork
</a>    </div>
    <div class="d-flex">
      <div class="flex-1 mr-2">
          <div class="d-block js-toggler-container js-social-container starring-container ">
    <form class="starred js-social-form" action="https://github.com/ZeyadZanaty/image-clustering/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="3qqYNMn/EQOedS2ReF8s8GQFEmJhUMevLicF9oX+UuZBqbnJQPIzt6KI8+7dUkH4jbybaNAB3CbOPuaugzF1Tw==">
      <input type="hidden" name="context" value="repository">
      <button type="submit" class="btn btn-sm  btn-block js-toggler-target" aria-label="Unstar this repository" title="Unstar ZeyadZanaty/image-clustering" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:161846877,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering?_pjax=%23js-repo-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="67f5313e251cab2e2b56072d768633e7e73ff9c837fd61ecabba19ec37c6cc47" data-ga-click="Repository, click unstar button, action:files#disambiguate; text:Unstar">        <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-star-fill mr-1">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"></path>
</svg>
        <span data-view-component="true">
          Unstar
</span></button></form>
    <form class="unstarred js-social-form" action="https://github.com/ZeyadZanaty/image-clustering/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="T3qYB8UmxVlEK6PDldfT3AT7oVNTm+eQGuMg2ds8l3LMypxxAZsyUVwMrodf7zkbouV9iopfRDaUNVZnUQ0Dsg==">
      <input type="hidden" name="context" value="repository">
      <button type="submit" class="btn btn-sm  btn-block js-toggler-target" aria-label="Unstar this repository" title="Star ZeyadZanaty/image-clustering" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:161846877,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering?_pjax=%23js-repo-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="9ed641f5374a03389343c9d3d0a5bdd89f945cd7cdd57ec5c086dea79a889e51" data-ga-click="Repository, click star button, action:files#disambiguate; text:Star">        <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-star mr-1">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg>
        <span data-view-component="true">
          Star
</span></button></form>  </div>

      </div>
      <div class="flex-1">
            <notifications-list-subscription-form class="f5 position-relative " data-catalyst="">
      <details class="details-reset details-overlay f5 position-relative" data-target="notifications-list-subscription-form.details" data-action="toggle:notifications-list-subscription-form#detailsToggled">

      <summary class="btn btn-sm btn-block" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:161846877,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering?_pjax=%23js-repo-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="66034410dadb6026955c76c51c03528351c44c1ee7a8a228965b13108a2865f5" data-ga-click="Repository, click Watch settings, action:files#disambiguate" aria-label="Notifications settings" aria-haspopup="menu" role="button">
          <span data-menu-button="">
            <span hidden="" data-target="notifications-list-subscription-form.unwatchButtonCopy">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-eye">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
              Unwatch
            </span>
            <span hidden="" data-target="notifications-list-subscription-form.stopIgnoringButtonCopy">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-bell-slash">
    <path fill-rule="evenodd" d="M8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 014.38 1.55 5 5 0 0113 5v2.373a.75.75 0 01-1.5 0V5A3.5 3.5 0 008 1.5zM4.182 4.31L1.19 2.143a.75.75 0 10-.88 1.214L3 5.305v2.642a.25.25 0 01-.042.139L1.255 10.64A1.518 1.518 0 002.518 13h11.108l1.184.857a.75.75 0 10.88-1.214l-1.375-.996a1.196 1.196 0 00-.013-.01L4.198 4.321a.733.733 0 00-.016-.011zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01.015.015 0 00.005.012.017.017 0 00.006.004l.007.001h9.037zM8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path>
</svg>
              Stop ignoring
            </span>
            <span data-target="notifications-list-subscription-form.watchButtonCopy">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-eye">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
              Watch
            </span>
          </span>
          <span class="dropdown-caret"></span>
</summary>
        <details-menu class="SelectMenu  " role="menu" data-target="notifications-list-subscription-form.menu">
          <div class="SelectMenu-modal notifications-component-menu-modal">
            <header class="SelectMenu-header">
              <h3 class="SelectMenu-title">Notifications</h3>
              <button class="SelectMenu-closeButton" type="button" aria-label="Close menu" data-action="click:notifications-list-subscription-form#closeMenu">
                <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
              </button>
            </header>

            <div class="SelectMenu-list">
              <form data-target="notifications-list-subscription-form.form" data-action="submit:notifications-list-subscription-form#submitForm" action="https://github.com/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="p5QGzltUhQ4OANufrZa1uprx6fNlSFTClh5ASeNfjrT138bK2gofUV7KMItKxCP88yC8E8UDGqAbCRV46yPOFg==">

                <input type="hidden" name="repository_id" value="161846877">

                <button type="submit" name="do" value="included" class="SelectMenu-item flex-items-start" role="menuitemradio" aria-checked="true" data-targets="notifications-list-subscription-form.subscriptionButtons">
                  <span class="f5">
                    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      Participating and @mentions
                    </div>
                    <div class="text-small color-text-secondary text-normal pb-1">
                      Only receive notifications from this repository when participating or @mentioned.
                    </div>
                  </div>
                </button>

                <button type="submit" name="do" value="subscribed" class="SelectMenu-item flex-items-start" role="menuitemradio" aria-checked="false" data-targets="notifications-list-subscription-form.subscriptionButtons">
                  <span class="f5">
                    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      All Activity
                    </div>
                    <div class="text-small color-text-secondary text-normal pb-1">
                      Notified of all notifications on this repository.
                    </div>
                  </div>
                </button>

                <button type="submit" name="do" value="ignore" class="SelectMenu-item flex-items-start" role="menuitemradio" aria-checked="false" data-targets="notifications-list-subscription-form.subscriptionButtons">
                  <span class="f5">
                    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      Ignore
                    </div>
                    <div class="text-small color-text-secondary text-normal pb-1">
                      Never be notified.
                    </div>
                  </div>
                </button>
</form>
              <button class="SelectMenu-item flex-items-start pr-3" type="button" role="menuitemradio" data-target="notifications-list-subscription-form.customButton" data-action="click:notifications-list-subscription-form#openCustomDialog" aria-haspopup="true" aria-checked="false">
                <span class="f5">
                  <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                </span>
                <div>
                  <div class="d-flex flex-items-start flex-justify-between">
                    <div class="f5 text-bold">Custom</div>
                    <div class="f5 pr-1">
                      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-arrow-right">
    <path fill-rule="evenodd" d="M8.22 2.97a.75.75 0 011.06 0l4.25 4.25a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06-1.06l2.97-2.97H3.75a.75.75 0 010-1.5h7.44L8.22 4.03a.75.75 0 010-1.06z"></path>
</svg>
                    </div>
                  </div>
                  <div class="text-small color-text-secondary text-normal pb-1">
                    Select events you want to be notified of in addition to participating and @mentions.
                  </div>
                </div>
              </button>
            </div>
          </div>
        </details-menu>

        <details-dialog class="notifications-component-dialog " data-target="notifications-list-subscription-form.customDialog" hidden="" role="dialog" aria-modal="true">
          <div class="SelectMenu-modal notifications-component-dialog-modal overflow-visible">
            <form data-target="notifications-list-subscription-form.customform" data-action="submit:notifications-list-subscription-form#submitCustomForm" action="https://github.com/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="ACiMZNdkyMHHOQmCdoEw5EGnByIBihEE66R9qkdonQpSY0xgVjpSnpfz4paR06aiKHZSwqHBX2ZmsyibTxTdqA==">

              <input type="hidden" name="repository_id" value="161846877">

              <header class="d-sm-none SelectMenu-header pb-0 border-bottom-0 px-2 px-sm-3">
                <h1 class="f3 SelectMenu-title d-inline-flex">
                  <button class="color-bg-primary border-0 px-2 py-0 m-0 Link--secondary f5" aria-label="Return to menu" type="button" data-action="click:notifications-list-subscription-form#closeCustomDialog">
                    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-arrow-left">
    <path fill-rule="evenodd" d="M7.78 12.53a.75.75 0 01-1.06 0L2.47 8.28a.75.75 0 010-1.06l4.25-4.25a.75.75 0 011.06 1.06L4.81 7h7.44a.75.75 0 010 1.5H4.81l2.97 2.97a.75.75 0 010 1.06z"></path>
</svg>
                  </button>
                  Custom
                </h1>
              </header>

              <header class="d-none d-sm-flex flex-items-start pt-1">
                <button class="border-0 px-2 pt-1 m-0 Link--secondary f5" style="background-color: transparent;" aria-label="Return to menu" type="button" data-action="click:notifications-list-subscription-form#closeCustomDialog">
                  <svg style="position: relative; left: 2px; top: 1px" aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-arrow-left">
    <path fill-rule="evenodd" d="M7.78 12.53a.75.75 0 01-1.06 0L2.47 8.28a.75.75 0 010-1.06l4.25-4.25a.75.75 0 011.06 1.06L4.81 7h7.44a.75.75 0 010 1.5H4.81l2.97 2.97a.75.75 0 010 1.06z"></path>
</svg>
                </button>

                <h1 class="pt-1 pr-4 pb-0 pl-0 f5 text-bold">
                  Custom
                </h1>
              </header>

              <fieldset>
                <legend>
                  <div class="text-small color-text-secondary pt-0 pr-3 pb-3 pl-6 pl-sm-5 border-bottom mb-3">
                    Select events you want to be notified of in addition to participating and @mentions.
                  </div>
                </legend>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="Issue" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Issues
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="PullRequest" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Pull requests
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="Release" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Releases
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="Discussion" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Discussions
                    </label>

                      <span class="tooltipped tooltipped-nw mr-2 p-1 float-right" aria-label="Discussions are not enabled for this repo">
                        <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-info color-icon-secondary">
    <path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm6.5-.25A.75.75 0 017.25 7h1a.75.75 0 01.75.75v2.75h.25a.75.75 0 010 1.5h-2a.75.75 0 010-1.5h.25v-2h-.25a.75.75 0 01-.75-.75zM8 6a1 1 0 100-2 1 1 0 000 2z"></path>
</svg>
                      </span>
                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input type="checkbox" name="thread_types[]" value="SecurityAlert" data-targets="notifications-list-subscription-form.threadTypeCheckboxes" data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated">
                      Security alerts
                    </label>

                  </div>
              </fieldset>
              <div class="pt-2 pb-3 px-3 d-flex flex-justify-start flex-row-reverse">
                <button type="submit" name="do" value="custom" class="btn btn-sm btn-primary ml-2" data-target="notifications-list-subscription-form.customSubmit" disabled="">Apply</button>

                <button class="btn btn-sm" type="button" data-action="click:notifications-list-subscription-form#resetForm" data-close-dialog="">Cancel</button>
              </div>
</form>          </div>
        </details-dialog>
        <div class="notifications-component-dialog-overlay"></div>
      </details>
    </notifications-list-subscription-form>



      </div>
    </div>
  </div>

        

  <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5 color-bg-secondary">

    <ul data-view-component="true" class="UnderlineNav-body list-style-none">
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/ZeyadZanaty/image-clustering" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /ZeyadZanaty/image-clustering" data-hotkey="g c" data-ga-click="Repository, Navigation click, Code tab" aria-current="page" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item selected">
    
                  <svg class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"></path></svg>
          <span data-content="Code">Code</span>
            <span title="Not available" data-view-component="true" class="Counter"></span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/ZeyadZanaty/image-clustering/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /ZeyadZanaty/image-clustering/issues" data-hotkey="g i" data-ga-click="Repository, Navigation click, Issues tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item">
    
                  <svg class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z"></path></svg>
          <span data-content="Issues">Issues</span>
            <span title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/ZeyadZanaty/image-clustering/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /ZeyadZanaty/image-clustering/pulls" data-hotkey="g p" data-ga-click="Repository, Navigation click, Pull requests tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item">
    
                  <svg class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"></path></svg>
          <span data-content="Pull requests">Pull requests</span>
            <span title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/ZeyadZanaty/image-clustering/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /ZeyadZanaty/image-clustering/actions" data-hotkey="g a" data-ga-click="Repository, Navigation click, Actions tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item">
    
                  <svg class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.379 5.227A.25.25 0 006 5.442v5.117a.25.25 0 00.379.214l4.264-2.559a.25.25 0 000-.428L6.379 5.227z"></path></svg>
          <span data-content="Actions">Actions</span>
            <span title="Not available" data-view-component="true" class="Counter"></span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/ZeyadZanaty/image-clustering/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /ZeyadZanaty/image-clustering/projects" data-hotkey="g b" data-ga-click="Repository, Navigation click, Projects tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item">
    
                  <svg class="octicon octicon-project UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
          <span data-content="Projects">Projects</span>
            <span title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/ZeyadZanaty/image-clustering/wiki" data-tab-item="i5wiki-tab" data-selected-links="repo_wiki /ZeyadZanaty/image-clustering/wiki" data-hotkey="g w" data-ga-click="Repository, Navigation click, Wikis tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item">
    
                  <svg class="octicon octicon-book UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 1.75A.75.75 0 01.75 1h4.253c1.227 0 2.317.59 3 1.501A3.744 3.744 0 0111.006 1h4.245a.75.75 0 01.75.75v10.5a.75.75 0 01-.75.75h-4.507a2.25 2.25 0 00-1.591.659l-.622.621a.75.75 0 01-1.06 0l-.622-.621A2.25 2.25 0 005.258 13H.75a.75.75 0 01-.75-.75V1.75zm8.755 3a2.25 2.25 0 012.25-2.25H14.5v9h-3.757c-.71 0-1.4.201-1.992.572l.004-7.322zm-1.504 7.324l.004-5.073-.002-2.253A2.25 2.25 0 005.003 2.5H1.5v9h3.757a3.75 3.75 0 011.994.574z"></path></svg>
          <span data-content="Wiki">Wiki</span>
            <span title="Not available" data-view-component="true" class="Counter"></span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/ZeyadZanaty/image-clustering/security" data-tab-item="i6security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /ZeyadZanaty/image-clustering/security" data-hotkey="g s" data-ga-click="Repository, Navigation click, Security tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item">
    
                  <svg class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.467.133a1.75 1.75 0 011.066 0l5.25 1.68A1.75 1.75 0 0115 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.7 1.7 0 01-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 011.217-1.667l5.25-1.68zm.61 1.429a.25.25 0 00-.153 0l-5.25 1.68a.25.25 0 00-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.2.2 0 00.154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.25.25 0 00-.174-.237l-5.25-1.68zM9 10.5a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.75a.75.75 0 10-1.5 0v3a.75.75 0 001.5 0v-3z"></path></svg>
          <span data-content="Security">Security</span>
            

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/ZeyadZanaty/image-clustering/pulse" data-tab-item="i7insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /ZeyadZanaty/image-clustering/pulse" data-ga-click="Repository, Navigation click, Insights tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item">
    
                  <svg class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 1.75a.75.75 0 00-1.5 0v12.5c0 .414.336.75.75.75h14.5a.75.75 0 000-1.5H1.5V1.75zm14.28 2.53a.75.75 0 00-1.06-1.06L10 7.94 7.53 5.47a.75.75 0 00-1.06 0L3.22 8.72a.75.75 0 001.06 1.06L7 7.06l2.47 2.47a.75.75 0 001.06 0l5.25-5.25z"></path></svg>
          <span data-content="Insights">Insights</span>
            <span title="Not available" data-view-component="true" class="Counter"></span>

    
</a></li>
</ul>
      <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions  js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <details data-view-component="true" class="details-overlay details-reset position-relative">
  <summary role="button" data-view-component="true">          <div class="UnderlineNav-item mr-0 border-0">
            <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
            <span class="sr-only">More</span>
          </div>
</summary>
  <div data-view-component="true">          <details-menu role="menu" data-view-component="true" class="dropdown-menu dropdown-menu-sw">
  
            <ul>
                <li data-menu-item="i0code-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" aria-current="page" data-selected-links=" /ZeyadZanaty/image-clustering" href="https://github.com/ZeyadZanaty/image-clustering">
                    Code
</a>                </li>
                <li data-menu-item="i1issues-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /ZeyadZanaty/image-clustering/issues" href="https://github.com/ZeyadZanaty/image-clustering/issues">
                    Issues
</a>                </li>
                <li data-menu-item="i2pull-requests-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /ZeyadZanaty/image-clustering/pulls" href="https://github.com/ZeyadZanaty/image-clustering/pulls">
                    Pull requests
</a>                </li>
                <li data-menu-item="i3actions-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /ZeyadZanaty/image-clustering/actions" href="https://github.com/ZeyadZanaty/image-clustering/actions">
                    Actions
</a>                </li>
                <li data-menu-item="i4projects-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /ZeyadZanaty/image-clustering/projects" href="https://github.com/ZeyadZanaty/image-clustering/projects">
                    Projects
</a>                </li>
                <li data-menu-item="i5wiki-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /ZeyadZanaty/image-clustering/wiki" href="https://github.com/ZeyadZanaty/image-clustering/wiki">
                    Wiki
</a>                </li>
                <li data-menu-item="i6security-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /ZeyadZanaty/image-clustering/security" href="https://github.com/ZeyadZanaty/image-clustering/security">
                    Security
</a>                </li>
                <li data-menu-item="i7insights-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /ZeyadZanaty/image-clustering/pulse" href="https://github.com/ZeyadZanaty/image-clustering/pulse">
                    Insights
</a>                </li>
            </ul>

</details-menu></div>
</details></div>
</nav>

  </div>


<div class="container-xl clearfix new-discussion-timeline px-3 px-md-4 px-lg-5">
  <div id="repo-content-pjax-container" class="repository-content ">


  
<div>
  


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="https://github.com/ZeyadZanaty/image-clustering/blob/b6854b43f9893bea692a2576cf41f9993c588ed2/DataReader.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v22:0d93ed96fb1b644a35bc99b7a32376f794f9fcffa9b66bfae9950366c79c27f3 -->

    <div class="d-flex flex-items-start flex-shrink-0 pb-3 flex-wrap flex-md-nowrap flex-justify-between flex-md-justify-start">
      
<div class="position-relative">
  <details class="details-reset details-overlay mr-0 mb-0 " id="branch-select-menu">
    <summary class="btn css-truncate" data-hotkey="w" title="Switch branches or tags">
      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-git-branch text-gray">
    <path fill-rule="evenodd" d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z"></path>
</svg>
      <span class="css-truncate-target" data-menu-button="">master</span>
      <span class="dropdown-caret"></span>
    </summary>

      
<div class="SelectMenu">
  <div class="SelectMenu-modal">
    <header class="SelectMenu-header">
      <span class="SelectMenu-title">Switch branches/tags</span>
      <button class="SelectMenu-closeButton" type="button" data-toggle-for="branch-select-menu"><svg aria-label="Close menu" aria-hidden="false" role="img" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg></button>
    </header>

    <input-demux data-action="tab-container-change:input-demux#storeInput tab-container-changed:input-demux#updateInput" data-catalyst="">
      <tab-container class="d-flex flex-column js-branches-tags-tabs" style="min-height: 0;">
        <div class="SelectMenu-filter">
          <input data-target="input-demux.source" id="context-commitish-filter-field" class="SelectMenu-input form-control" aria-owns="ref-list-branches" data-controls-ref-menu-id="ref-list-branches" autofocus="" autocomplete="off" aria-label="Filter branches/tags" placeholder="Filter branches/tags" type="text">
        </div>

        <div class="SelectMenu-tabs" role="tablist" data-target="input-demux.control">
          <button class="SelectMenu-tab" type="button" role="tab" aria-selected="true" tabindex="0">Branches</button>
          <button class="SelectMenu-tab" type="button" role="tab" aria-selected="false" tabindex="-1">Tags</button>
        </div>

        <div role="tabpanel" id="ref-list-branches" data-filter-placeholder="Filter branches/tags" class="d-flex flex-column flex-auto overflow-auto" tabindex="">
          <ref-selector type="branch" data-targets="input-demux.sinks" data-action="
              input-entered:ref-selector#inputEntered
              tab-selected:ref-selector#tabSelected
              focus-list:ref-selector#focusFirstListMember
            " query-endpoint="/ZeyadZanaty/image-clustering/refs" cache-key="v0:1544826395.0" current-committish="bWFzdGVy" default-branch="bWFzdGVy" name-with-owner="WmV5YWRaYW5hdHkvaW1hZ2UtY2x1c3RlcmluZw==" data-catalyst="">

            <template data-target="ref-selector.fetchFailedTemplate"></template>

              <template data-target="ref-selector.noMatchTemplate"></template>


            <!-- TODO: this max-height is necessary or else the branch list won't scroll.  why? -->
            <div data-target="ref-selector.listContainer" role="menu" class="SelectMenu-list " style="max-height: 330px">
              <div class="SelectMenu-loading pt-3 pb-0" aria-label="Menu is loading">
                <svg style="box-sizing: content-box; color: var(--color-icon-primary);" viewBox="0 0 16 16" fill="none" data-view-component="true" width="32" height="32" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
              </div>
            </div>

              <template data-target="ref-selector.itemTemplate"></template>


              <footer class="SelectMenu-footer"><a href="https://github.com/ZeyadZanaty/image-clustering/branches">View all branches</a></footer>
          </ref-selector>

        </div>

        <div role="tabpanel" id="tags-menu" data-filter-placeholder="Find a tag" class="d-flex flex-column flex-auto overflow-auto" tabindex="" hidden="">
          <ref-selector type="tag" data-action="
              input-entered:ref-selector#inputEntered
              tab-selected:ref-selector#tabSelected
              focus-list:ref-selector#focusFirstListMember
            " data-targets="input-demux.sinks" query-endpoint="/ZeyadZanaty/image-clustering/refs" cache-key="v0:1544826395.0" current-committish="bWFzdGVy" default-branch="bWFzdGVy" name-with-owner="WmV5YWRaYW5hdHkvaW1hZ2UtY2x1c3RlcmluZw==" data-catalyst="">

            <template data-target="ref-selector.fetchFailedTemplate"></template>

            <template data-target="ref-selector.noMatchTemplate"></template>

              <template data-target="ref-selector.itemTemplate"></template>


            <div data-target="ref-selector.listContainer" role="menu" class="SelectMenu-list" style="max-height: 330px">
              <div class="SelectMenu-loading pt-3 pb-0" aria-label="Menu is loading">
                <svg style="box-sizing: content-box; color: var(--color-icon-primary);" viewBox="0 0 16 16" fill="none" data-view-component="true" width="32" height="32" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
              </div>
            </div>
              <footer class="SelectMenu-footer"><a href="https://github.com/ZeyadZanaty/image-clustering/tags">View all tags</a></footer>
          </ref-selector>
        </div>
      </tab-container>
    </input-demux>
  </div>
</div>

  </details>

</div>

      <h2 id="blob-path" class="breadcrumb flex-auto flex-self-center min-width-0 text-normal mx-2 width-full width-md-auto flex-order-1 flex-md-order-none mt-3 mt-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="https://github.com/ZeyadZanaty/image-clustering"><span>image-clustering</span></a></span></span><span class="separator">/</span><strong class="final-path">DataReader.py</strong>
          <span class="separator">/</span><details class="details-reset details-overlay d-inline" id="jumpto-symbol-select-menu">
  <summary class="btn-link Link--secondary css-truncate" aria-haspopup="menu" data-hotkey="r" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_blob_definitions&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_blob_definitions&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="b18f87f28b9ed05e65915d0ba58576bc35538621c2973cf8dfab300a62541a8d" role="button">
      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-code">
    <path fill-rule="evenodd" d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"></path>
</svg>
    <span data-menu-button="">Jump to</span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="SelectMenu SelectMenu--hasFilter" role="menu">
    <div class="SelectMenu-modal">
      <header class="SelectMenu-header">
        <span class="SelectMenu-title">Code definitions</span>
        <button class="SelectMenu-closeButton" type="button" data-toggle-for="jumpto-symbol-select-menu">
          <svg aria-label="Close menu" role="img" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
        </button>
      </header>
        <div class="SelectMenu-filter">
          <input class="SelectMenu-input form-control js-filterable-field" id="jumpto-symbols-filter-field" type="text" autocomplete="off" spellcheck="false" autofocus="" placeholder="Filter definitions" aria-label="Filter definitions">
        </div>
      <div class="SelectMenu-list">
        <div data-filterable-for="jumpto-symbols-filter-field" data-filterable-type="substring">
            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="7080fec49dbdcb4ffd380180f858c182dc5f78e33aa370dcb0fcb2ae51ae479f" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py#L8">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">DataReader</span>
              <span class="flex-auto d-flex flex-justify-end">Class</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="7080fec49dbdcb4ffd380180f858c182dc5f78e33aa370dcb0fcb2ae51ae479f" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py#L10">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">__init__</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="7080fec49dbdcb4ffd380180f858c182dc5f78e33aa370dcb0fcb2ae51ae479f" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py#L14">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">get_dict_from_pickle</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="7080fec49dbdcb4ffd380180f858c182dc5f78e33aa370dcb0fcb2ae51ae479f" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py#L18">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">get_train_data</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="7080fec49dbdcb4ffd380180f858c182dc5f78e33aa370dcb0fcb2ae51ae479f" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py#L38">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">get_test_data</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="7080fec49dbdcb4ffd380180f858c182dc5f78e33aa370dcb0fcb2ae51ae479f" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py#L56">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">reshape_to_plot</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="7080fec49dbdcb4ffd380180f858c182dc5f78e33aa370dcb0fcb2ae51ae479f" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py#L61">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">plot_imgs</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="7080fec49dbdcb4ffd380180f858c182dc5f78e33aa370dcb0fcb2ae51ae479f" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py#L81">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">plot_img</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="7080fec49dbdcb4ffd380180f858c182dc5f78e33aa370dcb0fcb2ae51ae479f" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py#L93">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">read_mnist</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="7080fec49dbdcb4ffd380180f858c182dc5f78e33aa370dcb0fcb2ae51ae479f" href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py#L125">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">unpickle</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>        </div>
      </div>
      <footer class="SelectMenu-footer">
        <div class="d-flex flex-justify-between">
          Code navigation index up-to-date
          <svg class="octicon octicon-dot-fill text-green" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path></svg>
        </div>
      </footer>
    </div>
  </details-menu>
</details>

      </h2>
      <a href="https://github.com/ZeyadZanaty/image-clustering/find/master" class="js-pjax-capture-input btn mr-2 d-none d-md-block" data-pjax="" data-hotkey="t">
        Go to file
      </a>

      <details id="blob-more-options-details" data-view-component="true" class="details-overlay details-reset position-relative">
  <summary role="button" data-view-component="true" class="btn">
  
            <svg aria-label="More options" role="img" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>

  

</summary>
  <div data-view-component="true">          <ul class="dropdown-menu dropdown-menu-sw">
            <li class="d-block d-md-none">
              <a class="dropdown-item d-flex flex-items-baseline" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FIND_FILE_BUTTON&quot;,&quot;repository_id&quot;:161846877,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="54db7df72c566c003433555919cc50d9509104271b88c507275143425b16706e" data-ga-click="Repository, find file, location:repo overview" data-hotkey="t" data-pjax="true" href="https://github.com/ZeyadZanaty/image-clustering/find/master">
                <span class="flex-auto">Go to file</span>
                <span class="text-small color-text-secondary" aria-hidden="true">T</span>
</a>            </li>
            <li data-toggle-for="blob-more-options-details">
              <button type="button" data-toggle-for="jumpto-line-details-dialog" class="btn-link dropdown-item">
                <span class="d-flex flex-items-baseline">
                  <span class="flex-auto">Go to line</span>
                  <span class="text-small color-text-secondary" aria-hidden="true">L</span>
                </span>
              </button>
            </li>
            <li data-toggle-for="blob-more-options-details">
              <button type="button" data-toggle-for="jumpto-symbol-select-menu" class="btn-link dropdown-item">
                <span class="d-flex flex-items-baseline">
                  <span class="flex-auto">Go to definition</span>
                  <span class="text-small color-text-secondary" aria-hidden="true">R</span>
                </span>
              </button>
            </li>
            <li class="dropdown-divider" role="none"></li>
            <li>
              <clipboard-copy value="DataReader.py" class="dropdown-item cursor-pointer" data-toggle-for="blob-more-options-details" tabindex="0" role="button">
                Copy path
              </clipboard-copy>
            </li>
            <li>
              <clipboard-copy value="https://github.com/ZeyadZanaty/image-clustering/blob/b6854b43f9893bea692a2576cf41f9993c588ed2/DataReader.py" class="dropdown-item cursor-pointer" data-toggle-for="blob-more-options-details" tabindex="0" role="button">
                <span class="d-flex flex-items-baseline">
                  <span class="flex-auto">Copy permalink</span>
                </span>
              </clipboard-copy>
            </li>
          </ul>
</div>
</details>    </div>



    <div class="Box d-flex flex-column flex-shrink-0 mb-3">
      

  <div class="Box-header Box-header--blue Details js-details-container">
      <div class="d-flex flex-items-center">
        <span class="flex-shrink-0 ml-n1 mr-n1 mt-n1 mb-n1">
          <a rel="author" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/users/ZeyadZanaty/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ZeyadZanaty"><img class="avatar avatar-user" src="./DataReader_files/18510795" width="24" height="24" alt="@ZeyadZanaty"></a>
        </span>
        <div class="flex-1 d-flex flex-items-center ml-3 min-width-0">
          <div class="css-truncate css-truncate-overflow">
            <a class="text-bold Link--primary" rel="author" data-hovercard-type="user" data-hovercard-url="/users/ZeyadZanaty/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ZeyadZanaty">ZeyadZanaty</a>

                <span class="markdown-title">
                  <a data-pjax="true" title="Add F1 score measure" class="Link--secondary" href="https://github.com/ZeyadZanaty/image-clustering/commit/ed0b7bdd216c4fb95feed45380ab649881078a87">Add F1 score measure</a>
                </span>
          </div>


          <span class="ml-2">
            
          </span>
        </div>
        <div class="ml-3 d-flex flex-shrink-0 flex-items-center flex-justify-end color-text-secondary no-wrap">
          <span class="d-none d-md-inline">
            <span>Latest commit</span>
            <a class="text-small text-mono Link--secondary" href="https://github.com/ZeyadZanaty/image-clustering/commit/ed0b7bdd216c4fb95feed45380ab649881078a87" data-pjax="">ed0b7bd</a>
            <span itemprop="dateModified"><relative-time datetime="2018-12-20T23:24:30Z" class="no-wrap" title="Dec 21, 2018, 4:54 AM GMT+5:30">on Dec 21, 2018</relative-time></span>
          </span>

          <a data-pjax="" href="https://github.com/ZeyadZanaty/image-clustering/commits/master/DataReader.py" class="ml-3 no-wrap Link--primary no-underline">
            <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-history text-gray">
    <path fill-rule="evenodd" d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z"></path>
</svg>
            <span class="d-none d-sm-inline">
              <strong>History</strong>
            </span>
          </a>
        </div>
      </div>

  </div>

  <div class="Box-body d-flex flex-items-center flex-auto border-bottom-0 flex-wrap">
    <details class="details-reset details-overlay details-overlay-dark lh-default color-text-primary float-left mr-3" id="blob_contributors_box">
      <summary class="Link--primary" role="button">
        <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-people text-gray">
    <path fill-rule="evenodd" d="M5.5 3.5a2 2 0 100 4 2 2 0 000-4zM2 5.5a3.5 3.5 0 115.898 2.549 5.507 5.507 0 013.034 4.084.75.75 0 11-1.482.235 4.001 4.001 0 00-7.9 0 .75.75 0 01-1.482-.236A5.507 5.507 0 013.102 8.05 3.49 3.49 0 012 5.5zM11 4a.75.75 0 100 1.5 1.5 1.5 0 01.666 2.844.75.75 0 00-.416.672v.352a.75.75 0 00.574.73c1.2.289 2.162 1.2 2.522 2.372a.75.75 0 101.434-.44 5.01 5.01 0 00-2.56-3.012A3 3 0 0011 4z"></path>
</svg>
        <strong>1</strong>
        
        contributor
      </summary>
      <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast" aria-label="Users who have contributed to this file" src="/ZeyadZanaty/image-clustering/contributors-list/master/DataReader.py" preload="" role="dialog" aria-modal="true">
        <div class="Box-header">
          <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog="">
            <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
          </button>
          <h3 class="Box-title">
            Users who have contributed to this file
          </h3>
        </div>
        <include-fragment>
          <svg style="box-sizing: content-box; color: var(--color-icon-primary);" viewBox="0 0 16 16" fill="none" data-view-component="true" width="32" height="32" class="my-3 mx-auto d-block anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
        </include-fragment>
      </details-dialog>
    </details>
  </div>
    </div>




      







  
    <div data-target="readme-toc.content" class="Box mt-3 position-relative
    ">
      
  <div class="Box-header py-2 pr-2 d-flex flex-shrink-0 flex-md-row flex-items-center">


  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1">

      129 lines (119 sloc)
      <span class="file-info-divider"></span>
    5.01 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between hide-sm hide-md">

    <div class="BtnGroup">
      <a href="https://github.com/ZeyadZanaty/image-clustering/raw/master/DataReader.py" id="raw-url" role="button" data-view-component="true" class="btn-sm btn BtnGroup-item">
  
  Raw
  

</a>
        <a href="https://github.com/ZeyadZanaty/image-clustering/blame/master/DataReader.py" data-hotkey="b" role="button" data-view-component="true" class="js-update-url-with-hash btn-sm btn BtnGroup-item">
  
  Blame
  

</a>
    </div>

    <div>
          <a class="btn-octicon tooltipped tooltipped-nw js-remove-unless-platform" data-platforms="windows,mac" href="https://desktop.github.com/" aria-label="Open this file in GitHub Desktop" data-ga-click="Repository, open with desktop">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-device-desktop">
    <path fill-rule="evenodd" d="M1.75 2.5h12.5a.25.25 0 01.25.25v7.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25v-7.5a.25.25 0 01.25-.25zM14.25 1H1.75A1.75 1.75 0 000 2.75v7.5C0 11.216.784 12 1.75 12h3.727c-.1 1.041-.52 1.872-1.292 2.757A.75.75 0 004.75 16h6.5a.75.75 0 00.565-1.243c-.772-.885-1.193-1.716-1.292-2.757h3.727A1.75 1.75 0 0016 10.25v-7.5A1.75 1.75 0 0014.25 1zM9.018 12H6.982a5.72 5.72 0 01-.765 2.5h3.566a5.72 5.72 0 01-.765-2.5z"></path>
</svg>
          </a>

          <!-- '"` --><!-- </textarea></xmp> --><form class="inline-form js-update-url-with-hash" action="https://github.com/ZeyadZanaty/image-clustering/edit/master/DataReader.py" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="YtXdOUjHL3BALHw/UPdESLeosVToDypiHHEx/t9QlGogTo8uT57nen0gWSR+INuBFq6nlfYH74C1w21/S9oyZA==">
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit" aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with="">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-pencil">
    <path fill-rule="evenodd" d="M11.013 1.427a1.75 1.75 0 012.474 0l1.086 1.086a1.75 1.75 0 010 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 01-.927-.928l.929-3.25a1.75 1.75 0 01.445-.758l8.61-8.61zm1.414 1.06a.25.25 0 00-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 000-.354l-1.086-1.086zM11.189 6.25L9.75 4.81l-6.286 6.287a.25.25 0 00-.064.108l-.558 1.953 1.953-.558a.249.249 0 00.108-.064l6.286-6.286z"></path>
</svg>
            </button>
</form>
          <!-- '"` --><!-- </textarea></xmp> --><form class="inline-form" action="https://github.com/ZeyadZanaty/image-clustering/delete/master/DataReader.py" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="GfJ1wxYk1GkOTmYiyDu8+z8qco4kGINI0Gbfx3JC8BoyPX0GlVrj3c4WECudflnB6yhO1BEAWE5Q0cP11yaNTA==">
            <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit" aria-label="Fork this project and delete the file" data-disable-with="">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-trash">
    <path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path>
</svg>
            </button>
</form>    </div>
  </div>

    <div class="d-flex hide-lg hide-xl flex-order-2 flex-grow-0">
      <details class="dropdown details-reset details-overlay d-inline-block">
        <summary class="btn-octicon" aria-haspopup="true" aria-label="possible actions">
          <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
        </summary>

        <ul class="dropdown-menu dropdown-menu-sw">
            <li>
                <a class="dropdown-item tooltipped tooltipped-nw js-remove-unless-platform" data-platforms="windows,mac" href="https://desktop.github.com/" data-ga-click="Repository, open with desktop">
                  Open with Desktop
                </a>
            </li>
          <li>
            <a class="dropdown-item" href="https://github.com/ZeyadZanaty/image-clustering/raw/master/DataReader.py">
              View raw
            </a>
          </li>
            <li>
              <a class="dropdown-item" href="https://github.com/ZeyadZanaty/image-clustering/blame/master/DataReader.py">
                View blame
              </a>
            </li>

              <li class="dropdown-divider" role="none"></li>
              <li>
                <a class="dropdown-item" href="https://github.com/ZeyadZanaty/image-clustering/edit/master/DataReader.py">Edit file</a>
              </li>
              <li>
                <a class="dropdown-item menu-item-danger" href="https://github.com/ZeyadZanaty/image-clustering/delete/master/DataReader.py">Delete file</a>
              </li>
        </ul>
      </details>
    </div>
</div>


      
  <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python  gist-border-0">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8" data-paste-markdown-skip="">
      <tbody><tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">pickle</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">numpy</span> <span class="pl-k">as</span> <span class="pl-s1">np</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">os</span>.<span class="pl-s1">path</span> <span class="pl-k">import</span> <span class="pl-s1">join</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">os</span> <span class="pl-k">import</span> <span class="pl-s1">listdir</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">matplotlib</span>.<span class="pl-s1">pyplot</span> <span class="pl-k">as</span> <span class="pl-s1">plt</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">tqdm</span> <span class="pl-k">import</span> <span class="pl-s1">tqdm</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">struct</span> <span class="pl-k">as</span> <span class="pl-s1">st</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-v">DataReader</span>:</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">__init__</span>(<span class="pl-s1">self</span>,<span class="pl-s1">root_dir</span>,<span class="pl-s1">type</span><span class="pl-c1">=</span><span class="pl-s">'cifar-100'</span>):</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">self</span>.<span class="pl-s1">root_dir</span> <span class="pl-c1">=</span> <span class="pl-s1">root_dir</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">self</span>.<span class="pl-s1">type</span> <span class="pl-c1">=</span> <span class="pl-s1">type</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_dict_from_pickle</span>(<span class="pl-s1">self</span>):</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">self</span>.<span class="pl-s1">train_dict</span> <span class="pl-c1">=</span> <span class="pl-en">unpickle</span>(<span class="pl-en">join</span>(<span class="pl-s1">self</span>.<span class="pl-s1">root_dir</span>,<span class="pl-s">'train'</span>))</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">self</span>.<span class="pl-s1">test_dict</span> <span class="pl-c1">=</span> <span class="pl-en">unpickle</span>(<span class="pl-en">join</span>(<span class="pl-s1">self</span>.<span class="pl-s1">root_dir</span>,<span class="pl-s">'test'</span>))</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_train_data</span>(<span class="pl-s1">self</span>):</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s1">self</span>.<span class="pl-s1">type</span> <span class="pl-c1">==</span> <span class="pl-s">'cifar-100'</span>:</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">self</span>.<span class="pl-en">get_dict_from_pickle</span>()</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">data</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-en">array</span>(<span class="pl-s1">self</span>.<span class="pl-s1">train_dict</span>[<span class="pl-s">b'data'</span>])</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">lbls_sub</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-en">array</span>(<span class="pl-s1">self</span>.<span class="pl-s1">train_dict</span>[<span class="pl-s">b'fine_labels'</span>])</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">lbls_class</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-en">array</span>(<span class="pl-s1">self</span>.<span class="pl-s1">train_dict</span>[<span class="pl-s">b'coarse_labels'</span>])</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s1">data</span>,<span class="pl-s1">lbls_class</span>,<span class="pl-s1">lbls_sub</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-s1">self</span>.<span class="pl-s1">type</span> <span class="pl-c1">==</span> <span class="pl-s">'cifar-10'</span>:</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">data</span> <span class="pl-c1">=</span> []</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">labels</span> <span class="pl-c1">=</span> []</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">            <span class="pl-en">print</span>(<span class="pl-s">"Reading"</span>)</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> <span class="pl-s1">file_</span> <span class="pl-c1">in</span> <span class="pl-en">tqdm</span>(<span class="pl-en">listdir</span>(<span class="pl-s1">self</span>.<span class="pl-s1">root_dir</span>)):</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-s1">file_</span>.<span class="pl-en">split</span>(<span class="pl-s">'_'</span>)[<span class="pl-c1">0</span>] <span class="pl-c1">==</span> <span class="pl-s">'data'</span>:</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s1">dict</span> <span class="pl-c1">=</span> <span class="pl-en">unpickle</span>(<span class="pl-en">join</span>(<span class="pl-s1">self</span>.<span class="pl-s1">root_dir</span>,<span class="pl-s1">file_</span>))</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s1">data</span>.<span class="pl-en">extend</span>(<span class="pl-s1">dict</span>[<span class="pl-s">b'data'</span>])</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s1">labels</span>.<span class="pl-en">extend</span>(<span class="pl-s1">dict</span>[<span class="pl-s">b'labels'</span>])</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s1">np</span>.<span class="pl-en">array</span>(<span class="pl-s1">data</span>),<span class="pl-s1">np</span>.<span class="pl-en">array</span>(<span class="pl-s1">labels</span>),<span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-s1">self</span>.<span class="pl-s1">type</span> <span class="pl-c1">==</span><span class="pl-s">'mnist'</span>:</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s1">self</span>.<span class="pl-en">read_mnist</span>()</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_test_data</span>(<span class="pl-s1">self</span>):</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s1">self</span>.<span class="pl-s1">type</span> <span class="pl-c1">==</span> <span class="pl-s">'cifar-100'</span>:</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">self</span>.<span class="pl-en">get_dict_from_pickle</span>()</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">data</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-en">array</span>(<span class="pl-s1">self</span>.<span class="pl-s1">test_dict</span>[<span class="pl-s">b'data'</span>])</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">lbls_sub</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-en">array</span>(<span class="pl-s1">self</span>.<span class="pl-s1">test_dict</span>[<span class="pl-s">b'fine_labels'</span>])</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">lbls_class</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-en">array</span>(<span class="pl-s1">self</span>.<span class="pl-s1">test_dict</span>[<span class="pl-s">b'coarse_labels'</span>])</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s1">data</span>,<span class="pl-s1">lbls_class</span>,<span class="pl-s1">lbls_sub</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-s1">self</span>.<span class="pl-s1">type</span> <span class="pl-c1">==</span> <span class="pl-s">'cifar-10'</span>:</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">data</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-en">empty</span>(<span class="pl-s1">shape</span><span class="pl-c1">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">3072</span>))</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">labels</span> <span class="pl-c1">=</span> []</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> <span class="pl-s1">file_</span> <span class="pl-c1">in</span> <span class="pl-en">listdir</span>(<span class="pl-s1">self</span>.<span class="pl-s1">root_dir</span>):</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-s1">file_</span>.<span class="pl-en">split</span>(<span class="pl-s">'_'</span>)[<span class="pl-c1">0</span>] <span class="pl-c1">==</span> <span class="pl-s">'test'</span>:</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s1">dict</span> <span class="pl-c1">=</span> <span class="pl-en">unpickle</span>(<span class="pl-en">join</span>(<span class="pl-s1">self</span>.<span class="pl-s1">root_dir</span>,<span class="pl-s1">file_</span>))</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s1">data</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-en">vstack</span>((<span class="pl-s1">data</span>,<span class="pl-s1">dict</span>[<span class="pl-s">b'data'</span>]))</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">                    <span class="pl-en">print</span>(<span class="pl-s1">data</span>[<span class="pl-s1">data</span>.<span class="pl-s1">shape</span>[<span class="pl-c1">0</span>]<span class="pl-c1">-</span><span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s1">labels</span>.<span class="pl-en">append</span>(<span class="pl-s1">dict</span>[<span class="pl-s">b'labels'</span>])</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s1">np</span>.<span class="pl-en">array</span>(<span class="pl-s1">data</span>),<span class="pl-s1">np</span>.<span class="pl-en">array</span>(<span class="pl-s1">labels</span>),<span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">reshape_to_plot</span>(<span class="pl-s1">self</span>,<span class="pl-s1">data</span>):</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s1">self</span>.<span class="pl-s1">type</span> <span class="pl-c1">==</span> <span class="pl-s">'mnist'</span>:</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s1">data</span>.<span class="pl-en">reshape</span>(<span class="pl-s1">data</span>.<span class="pl-s1">shape</span>[<span class="pl-c1">0</span>],<span class="pl-c1">28</span>,<span class="pl-c1">28</span>).<span class="pl-en">astype</span>(<span class="pl-s">"uint8"</span>)</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-s1">data</span>.<span class="pl-en">reshape</span>(<span class="pl-s1">data</span>.<span class="pl-s1">shape</span>[<span class="pl-c1">0</span>],<span class="pl-c1">3</span>,<span class="pl-c1">32</span>,<span class="pl-c1">32</span>).<span class="pl-en">transpose</span>(<span class="pl-c1">0</span>,<span class="pl-c1">2</span>,<span class="pl-c1">3</span>,<span class="pl-c1">1</span>).<span class="pl-en">astype</span>(<span class="pl-s">"uint8"</span>)</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">plot_imgs</span>(<span class="pl-s1">self</span>,<span class="pl-s1">in_data</span>,<span class="pl-s1">n</span>,<span class="pl-s1">random</span><span class="pl-c1">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">data</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-en">array</span>([<span class="pl-s1">d</span> <span class="pl-k">for</span> <span class="pl-s1">d</span> <span class="pl-c1">in</span> <span class="pl-s1">in_data</span>])</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">data</span> <span class="pl-c1">=</span> <span class="pl-s1">self</span>.<span class="pl-en">reshape_to_plot</span>(<span class="pl-s1">data</span>)</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">x1</span> <span class="pl-c1">=</span> <span class="pl-en">min</span>(<span class="pl-s1">n</span><span class="pl-c1">//</span><span class="pl-c1">2</span>,<span class="pl-c1">5</span>)</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s1">x1</span> <span class="pl-c1">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">x1</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">y1</span> <span class="pl-c1">=</span> (<span class="pl-s1">n</span><span class="pl-c1">//</span><span class="pl-s1">x1</span>)</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">x</span> <span class="pl-c1">=</span> <span class="pl-en">min</span>(<span class="pl-s1">x1</span>,<span class="pl-s1">y1</span>)</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">y</span> <span class="pl-c1">=</span> <span class="pl-en">max</span>(<span class="pl-s1">x1</span>,<span class="pl-s1">y1</span>)</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">fig</span>, <span class="pl-s1">ax</span> <span class="pl-c1">=</span> <span class="pl-s1">plt</span>.<span class="pl-en">subplots</span>(<span class="pl-s1">x</span>,<span class="pl-s1">y</span>,<span class="pl-s1">figsize</span><span class="pl-c1">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">5</span>))</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">i</span><span class="pl-c1">=</span><span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">j</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-s1">x</span>):</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> <span class="pl-s1">k</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-s1">y</span>):</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-s1">random</span>:</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s1">i</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-s1">random</span>.<span class="pl-en">choice</span>(<span class="pl-en">range</span>(<span class="pl-en">len</span>(<span class="pl-s1">data</span>)))</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">                <span class="pl-s1">ax</span>[<span class="pl-s1">j</span>][<span class="pl-s1">k</span>].<span class="pl-en">set_axis_off</span>()</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">                <span class="pl-s1">ax</span>[<span class="pl-s1">j</span>][<span class="pl-s1">k</span>].<span class="pl-en">imshow</span>(<span class="pl-s1">data</span>[<span class="pl-s1">i</span>:<span class="pl-s1">i</span><span class="pl-c1">+</span><span class="pl-c1">1</span>][<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">                <span class="pl-s1">i</span><span class="pl-c1">+=</span><span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">plt</span>.<span class="pl-en">show</span>()</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">plot_img</span>(<span class="pl-s1">self</span>,<span class="pl-s1">data</span>):</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s1">self</span>.<span class="pl-s1">type</span> <span class="pl-c1">!=</span><span class="pl-s">'mnist'</span>:</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">assert</span> <span class="pl-s1">data</span>.<span class="pl-s1">shape</span> <span class="pl-c1">==</span> (<span class="pl-c1">3072</span>,)</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">data</span> <span class="pl-c1">=</span> <span class="pl-s1">data</span>.<span class="pl-en">reshape</span>(<span class="pl-c1">1</span>,<span class="pl-c1">3072</span>)</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">data</span> <span class="pl-c1">=</span> <span class="pl-s1">data</span>.<span class="pl-en">reshape</span>(<span class="pl-s1">data</span>.<span class="pl-s1">shape</span>[<span class="pl-c1">0</span>],<span class="pl-c1">3</span>,<span class="pl-c1">32</span>,<span class="pl-c1">32</span>).<span class="pl-en">transpose</span>(<span class="pl-c1">0</span>,<span class="pl-c1">2</span>,<span class="pl-c1">3</span>,<span class="pl-c1">1</span>).<span class="pl-en">astype</span>(<span class="pl-s">"uint8"</span>)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-s1">self</span>.<span class="pl-s1">type</span> <span class="pl-c1">==</span> <span class="pl-s">'mnist'</span>:</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">assert</span> <span class="pl-s1">data</span>.<span class="pl-s1">shape</span> <span class="pl-c1">==</span> (<span class="pl-c1">28</span><span class="pl-c1">*</span><span class="pl-c1">28</span>,)</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">data</span> <span class="pl-c1">=</span> <span class="pl-s1">data</span>.<span class="pl-en">reshape</span>(<span class="pl-c1">1</span>,<span class="pl-c1">28</span>,<span class="pl-c1">28</span>).<span class="pl-en">astype</span>(<span class="pl-s">'uint8'</span>)</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">fig</span>, <span class="pl-s1">ax</span> <span class="pl-c1">=</span> <span class="pl-s1">plt</span>.<span class="pl-en">subplots</span>(<span class="pl-s1">figsize</span><span class="pl-c1">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">5</span>))</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">ax</span>.<span class="pl-en">imshow</span>(<span class="pl-s1">data</span>[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">plt</span>.<span class="pl-en">show</span>()</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">read_mnist</span>(<span class="pl-s1">self</span>):  </td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">filename</span> <span class="pl-c1">=</span> {<span class="pl-s">'images'</span> : <span class="pl-s">'train-images-idx3-ubyte'</span> ,<span class="pl-s">'labels'</span> : <span class="pl-s">'train-labels-idx1-ubyte'</span>}</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">labels_array</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-en">array</span>([])</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">data_types</span> <span class="pl-c1">=</span> {</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">0x08</span>: (<span class="pl-s">'ubyte'</span>, <span class="pl-s">'B'</span>, <span class="pl-c1">1</span>),</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">0x09</span>: (<span class="pl-s">'byte'</span>, <span class="pl-s">'b'</span>, <span class="pl-c1">1</span>),</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">0x0B</span>: (<span class="pl-s">'&gt;i2'</span>, <span class="pl-s">'h'</span>, <span class="pl-c1">2</span>),</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">0x0C</span>: (<span class="pl-s">'&gt;i4'</span>, <span class="pl-s">'i'</span>, <span class="pl-c1">4</span>),</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">0x0D</span>: (<span class="pl-s">'&gt;f4'</span>, <span class="pl-s">'f'</span>, <span class="pl-c1">4</span>),</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">0x0E</span>: (<span class="pl-s">'&gt;f8'</span>, <span class="pl-s">'d'</span>, <span class="pl-c1">8</span>)}</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">name</span> <span class="pl-c1">in</span> <span class="pl-s1">filename</span>.<span class="pl-en">keys</span>():</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-s1">name</span> <span class="pl-c1">==</span> <span class="pl-s">'images'</span>:</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">                <span class="pl-s1">imagesfile</span> <span class="pl-c1">=</span> <span class="pl-en">open</span>(<span class="pl-en">join</span>(<span class="pl-s1">self</span>.<span class="pl-s1">root_dir</span>,<span class="pl-s1">filename</span>[<span class="pl-s1">name</span>]),<span class="pl-s">'rb'</span>)</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-s1">name</span> <span class="pl-c1">==</span> <span class="pl-s">'labels'</span>:</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">                <span class="pl-s1">labelsfile</span> <span class="pl-c1">=</span> <span class="pl-en">open</span>(<span class="pl-en">join</span>(<span class="pl-s1">self</span>.<span class="pl-s1">root_dir</span>,<span class="pl-s1">filename</span>[<span class="pl-s1">name</span>]),<span class="pl-s">'rb'</span>)</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">imagesfile</span>.<span class="pl-en">seek</span>(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">magic</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">unpack</span>(<span class="pl-s">'&gt;4B'</span>,<span class="pl-s1">imagesfile</span>.<span class="pl-en">read</span>(<span class="pl-c1">4</span>))</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span>(<span class="pl-s1">magic</span>[<span class="pl-c1">0</span>] <span class="pl-c1">and</span> <span class="pl-s1">magic</span>[<span class="pl-c1">1</span>])<span class="pl-c1">or</span>(<span class="pl-s1">magic</span>[<span class="pl-c1">2</span>] <span class="pl-c1">not</span> <span class="pl-c1">in</span> <span class="pl-s1">data_types</span>):</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">raise</span> <span class="pl-v">ValueError</span>(<span class="pl-s">"File Format not correct"</span>)</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">nDim</span> <span class="pl-c1">=</span> <span class="pl-s1">magic</span>[<span class="pl-c1">3</span>]</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">imagesfile</span>.<span class="pl-en">seek</span>(<span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">nImg</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">unpack</span>(<span class="pl-s">'&gt;I'</span>,<span class="pl-s1">imagesfile</span>.<span class="pl-en">read</span>(<span class="pl-c1">4</span>))[<span class="pl-c1">0</span>] <span class="pl-c">#num of images/labels</span></td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">nR</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">unpack</span>(<span class="pl-s">'&gt;I'</span>,<span class="pl-s1">imagesfile</span>.<span class="pl-en">read</span>(<span class="pl-c1">4</span>))[<span class="pl-c1">0</span>] <span class="pl-c">#num of rows</span></td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">nC</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">unpack</span>(<span class="pl-s">'&gt;I'</span>,<span class="pl-s1">imagesfile</span>.<span class="pl-en">read</span>(<span class="pl-c1">4</span>))[<span class="pl-c1">0</span>] <span class="pl-c">#num of columns</span></td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">nBytes</span> <span class="pl-c1">=</span> <span class="pl-s1">nImg</span><span class="pl-c1">*</span><span class="pl-s1">nR</span><span class="pl-c1">*</span><span class="pl-s1">nC</span></td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">labelsfile</span>.<span class="pl-en">seek</span>(<span class="pl-c1">8</span>) <span class="pl-c">#Since no. of items = no. of images and is already read</span></td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">images_array</span> <span class="pl-c1">=</span> <span class="pl-c1">255</span> <span class="pl-c1">-</span> <span class="pl-s1">np</span>.<span class="pl-en">asarray</span>(<span class="pl-s1">st</span>.<span class="pl-en">unpack</span>(<span class="pl-s">'&gt;'</span><span class="pl-c1">+</span><span class="pl-s">'B'</span><span class="pl-c1">*</span><span class="pl-s1">nBytes</span>,<span class="pl-s1">imagesfile</span>.<span class="pl-en">read</span>(<span class="pl-s1">nBytes</span>))).<span class="pl-en">reshape</span>((<span class="pl-s1">nImg</span>,<span class="pl-s1">nR</span>,<span class="pl-s1">nC</span>))</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">labels_array</span> <span class="pl-c1">=</span> <span class="pl-s1">np</span>.<span class="pl-en">asarray</span>(<span class="pl-s1">st</span>.<span class="pl-en">unpack</span>(<span class="pl-s">'&gt;'</span><span class="pl-c1">+</span><span class="pl-s">'B'</span><span class="pl-c1">*</span><span class="pl-s1">nImg</span>,<span class="pl-s1">labelsfile</span>.<span class="pl-en">read</span>(<span class="pl-s1">nImg</span>))).<span class="pl-en">reshape</span>((<span class="pl-s1">nImg</span>,<span class="pl-c1">1</span>))</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">labels_array</span> <span class="pl-c1">=</span> [<span class="pl-s1">l</span>[<span class="pl-c1">0</span>] <span class="pl-k">for</span> <span class="pl-s1">l</span> <span class="pl-c1">in</span> <span class="pl-s1">labels_array</span>]</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-s1">images_array</span>.<span class="pl-en">reshape</span>(<span class="pl-c1">60000</span>,<span class="pl-c1">28</span><span class="pl-c1">*</span><span class="pl-c1">28</span>),<span class="pl-s1">labels_array</span>,<span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">unpickle</span>(<span class="pl-s1">file</span>):</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> <span class="pl-s1">pickle</span></td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s1">file</span>, <span class="pl-s">'rb'</span>) <span class="pl-k">as</span> <span class="pl-s1">fo</span>:</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">dict</span> <span class="pl-c1">=</span> <span class="pl-s1">pickle</span>.<span class="pl-en">load</span>(<span class="pl-s1">fo</span>, <span class="pl-s1">encoding</span><span class="pl-c1">=</span><span class="pl-s">'bytes'</span>)</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-s1">dict</span></td>
      </tr>
</tbody></table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 color-bg-primary border color-border-tertiary rounded-1" aria-label="Inline file action toolbar" aria-haspopup="menu" role="button">
      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
    </summary>
    <details-menu role="menu">
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" tabindex="0">
            Copy lines
          </clipboard-copy>
        </li>
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" tabindex="0">
            Copy permalink
          </clipboard-copy>
        </li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="https://github.com/ZeyadZanaty/image-clustering/blame/b6854b43f9893bea692a2576cf41f9993c588ed2/DataReader.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="https://github.com/ZeyadZanaty/image-clustering/issues/new">Reference in new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>


  

  <details class="details-reset details-overlay details-overlay-dark" id="jumpto-line-details-dialog">
    <summary data-hotkey="l" aria-label="Jump to line" role="button"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line" role="dialog" aria-modal="true">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-jump-to-line-form Box-body d-flex" action="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py" accept-charset="UTF-8" method="get">
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line…" aria-label="Jump to line" autofocus="">
        <button type="submit" class="btn" data-close-dialog="">Go</button>
</form>    </details-dialog>
  </details>

    <div class="Popover anim-scale-in js-tagsearch-popover" hidden="" data-tagsearch-url="/ZeyadZanaty/image-clustering/find-definition" data-tagsearch-ref="master" data-tagsearch-path="DataReader.py" data-tagsearch-lang="Python" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_symbol&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_symbol&quot;,&quot;repository_id&quot;:161846877,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:57684736}}" data-hydro-click-hmac="1b4ed1adae63bb494c27084535512aa7a9d3306e0298a258e4236194557bc10d">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box color-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>


</div>















</div>
</div>















</main>
  </div>

  </div>

          
<div class="footer container-xl width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 color-text-secondary border-top color-border-secondary ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">© 2021 GitHub, Inc.</li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/en/github/site-policy/github-terms-of-service" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/en/github/site-policy/github-privacy-statement" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://www.githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:Docs" href="https://docs.github.com/">Docs</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com/">
      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="24" width="24" class="octicon octicon-mark-github">
    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
</svg>
</a>
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a href="https://support.github.com/" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://services.github.com/" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog/" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 color-text-tertiary"></span>
  </div>

  
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden="">
    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a href="https://github.com/ZeyadZanaty/image-clustering/blob/master/DataReader.py">Reload</a> to refresh your session.</span>
  </div>
    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>



  

  


<div aria-live="polite" class="sr-only">Loading complete</div></body><div id="huntr-react-container-2"></div></html>