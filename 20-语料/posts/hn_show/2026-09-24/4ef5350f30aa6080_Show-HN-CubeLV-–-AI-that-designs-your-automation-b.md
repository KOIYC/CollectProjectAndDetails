---
type: "corpus"
item_id: "4ef5350f30aa6080"
title: "Show HN: CubeLV – AI that designs your automation before building it"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49827478"
project_url: "https://app.cubelv.com/"
author: "qqrun"
published_at: "2026-09-24T07:39:23Z"
captured_at: "2026-09-25T13:54:35+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-24"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_qqrun
  - story_49827478
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: CubeLV – AI that designs your automation before building it

> [!info] 一句话导读
> // 公開分享頁 origin 轉址：未登入者一律去公開頁 origin 看。

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49827478>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：qqrun　|　发布：2026-09-24T07:39:23Z
> 项目链接：<https://app.cubelv.com/>
> 采集：2026-09-25T13:54:35+08:00　|　id：`4ef5350f30aa6080`

## 正文

AStockTeam

 // 公開分享頁 origin 轉址：未登入者一律去公開頁 origin 看。
 //
 // 分享連結一律產生 app origin（已登入者點開直接開啟，不必多按登入），未登入者才轉走。
 // 登入態只存在 localStorage，CloudFront / Lambda@Edge 讀不到，所以這個判斷只能在
 // 瀏覽器做 —— 也因此爬蟲（不跑 JS）永遠停在 app origin，兩邊的 /share/ 都要掛 share-ogp。
 //
 // 擺在 head 最前面、bundle 下載之前：匿名訪客是分享連結的大宗，讓他們先拉完整份 SPA
 // 再轉走等於每次點擊都白下載一次。
 // 兩個 origin 相同時（dev）整段不動作；Electron / Capacitor 的 origin 也對不上，自動略過。
 (function () {
 var appOrigin = 'https://astockteam.ai';
 var publicOrigin = 'https://astockteam.com';
 if (publicOrigin === appOrigin) return;
 if (location.origin !== appOrigin) return;
 if (!/^\/share\/[a-f0-9]{24}/.test(location.pathname)) return;
 try {
 if (localStorage.getItem('isLoggedIn') === 'true') return;
 } catch (e) { /* localStorage 不可用（隱私模式）→ 當作未登入 */ }
 location.replace(publicOrigin + location.pathname + location.search + location.hash);
 })();

 @layer theme, base, components, utilities;

 // Android Capacitor 8 SystemBars：原生只在 DOMContentLoaded 才呼叫 onDOMReady（native-bridge.js），
 // 那刻 WebView 才從「padded 避開 system bar（innerHeight 矮）」切成「edge-to-edge passthrough（innerHeight 全高）」，
 // 造成啟動 ~700ms 整個 viewport 高度跳變、畫面被往上頂一下。
 // 這裡在第一幀就提早呼叫，meta viewport（viewport-fit=cover）已在 DOM，原生立即檢測到 cover 並 requestApplyInsets，
 // WebView 從頭就 edge-to-edge，消除跳變。idempotent：Capacitor 之後 DOMContentLoaded 再呼一次無副作用。
 (function () {
 try {
 var i = window.CapacitorSystemBarsAndroidInterface;
 if (i && typeof i.onDOMReady === 'function') i.onDOMReady();
 } catch (e) {}
 })();

 // Capacitor native shell：強制移除任何舊版 PWA service worker + cache。
 // 先前 build 開過 PWA，user 設備上的 SW 已 active，會 intercept 新 chunk fetch；
 // 偵測到 SW 就 unregister + 清 caches + reload 一次（sessionStorage flag 避免無限 reload）。
 (function () {
 var cap = window.Capacitor;
 var isNative = cap && typeof cap.isNativePlatform === 'function' && cap.isNativePlatform();
 if (!isNative || !navigator.serviceWorker) return;
 navigator.serviceWorker.register = function () { return Promise.resolve(); };
 if (!navigator.serviceWorker.getRegistrations) return;
 navigator.serviceWorker.getRegistrations().then(function (regs) {
 if (regs.length === 0) return;
 var unregAll = Promise.all(regs.map(function (r) { return r.unregister().catch(function () {}); }));
 var clearCaches = (typeof caches !== 'undefined' && caches.keys)
 ? caches.keys().then(function (names) { return Promise.all(names.map(function (n) { return caches.delete(n).catch(function () {}); })); }).catch(function () {})
 : Promise.resolve();
 Promise.all([unregAll, clearCaches]).then(function () {
 if (sessionStorage.getItem('sw-cleared') === '1') return;
 sessionStorage.setItem('sw-cleared', '1');
 window.location.reload();
 });
 }).catch(function () {});
 })();

 // 立即決定主題並設置 favicon（必須在最前面執行）
 (function() {
 var saved = localStorage.getItem('themeMode');
 var theme;
 if (window.location.pathname.replace(/\/$/, '') === '/wall') {
 theme = 'light';
 } else if (saved === 'light' || saved === 'dark') {
 theme = saved;
 } else {
 theme = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
 }
 var html = document.documentElement;
 html.classList.remove('theme-light', 'theme-dark');
 html.classList.add('theme-' + theme);
 })();

 /* @font-face 讓 CSS engine 直接認識字型 → browser 在 visibility:hidden 元素存在時即開始抓字型，
 消除 Android WebView 上 document.fonts.add() 無法讓 CSS engine 使用字型的問題。
 JS FontFace.load()（見下方 script）只負責時序：確認字型真正載完後才顯示圖示。 */
 @font-face {
 font-family: 'Material Symbols Outlined';
 src: url('/fonts/MaterialSymbolsOutlined.woff2') format('woff2');
 font-style: normal;
 font-weight: 100 700;
 font-display: block;
 }
 /* 在字體載入前隱藏 Material Symbols，避免顯示文字（FOUT）。
 不設 font-size:0 —— 有 visibility:hidden 就能防止 FOUT，
 且 browser 對 font-size:0 的元素不會主動抓字型，造成 race condition。 */
 .material-symbols-outlined {
 font-family: 'Material Symbols Outlined';
 visibility: hidden;
 }
 .g-icon {
 font-family: 'Material Symbols Outlined';
 visibility: hidden !important;
 }
 /* loading 階段跟主題深淺（theme-* class 由上方主題腳本設定）；React 進主畫面後 .app 元素用 var(--background) 蓋過
 * html/body 背景，所以這裡只影響 React mount 前的 fallback。 */
 html, body {
 margin: 0;
 padding: 0;
 background-color: #f6f6f6;
 }
 html.theme-dark, html.theme-dark body {
 background-color: #1C2127;
 }
 /* App 級 safe-area 變數（全 codebase 唯一來源，元件禁止直接寫 env()）。
 Android WebView 的 env(safe-area-inset-*) 來自 display cutout，不含狀態列；
 小米/POCO（HyperOS）藏開孔時 cutout=0 → env 全 0，頂欄會畫進狀態列底下。
 Capacitor 8 SystemBars 會把 systemBars∪cutout 的正確值注入成 --safe-area-inset-*
 （inline style on ，Android 15+），取兩者 max：注入值罩 HyperOS，env 罩 iOS/web。 */
 :root {
 --app-inset-top: max(var(--safe-area-inset-top, 0px), var(--native-inset-top, 0px), env(safe-area-inset-top, 0px));
 --app-inset-bottom: max(var(--safe-area-inset-bottom, 0px), var(--native-inset-bottom, 0px), env(safe-area-inset-bottom, 0px));
 --app-inset-left: max(var(--safe-area-inset-left, 0px), var(--native-inset-left, 0px), env(safe-area-inset-left, 0px));
 --app-inset-right: max(var(--safe-area-inset-right, 0px), var(--native-inset-right, 0px), env(safe-area-inset-right, 0px));
 /* app 之上還有另一層頁首時（公開分享頁的標題列），由該層量出自己的高度覆寫此值。
 覆蓋層（地圖等）用 var(--app-chrome-top) 定位，跟頁首切齊；
 浮動橫條再加 var(--app-chrome-gap) 拉開一點，不然看起來像疊在頁首上。 */
 --app-chrome-top: 0px;
 --app-chrome-gap: 0px;
 }

 /* Android：WebView 的 env(safe-area-inset-*) 只反映 display cutout，多數機型（含模擬器）
 回 0，內容會整片畫進狀態列底下。原生 MainActivity 量到 systemBars∪cutout 後開
 CubeLVSafeArea 介面，這裡在文件一建立就取值寫進 --safe-area-inset-*（index.html 的
 --app-inset-* 取它與 env 的 max）。insets 變動（旋轉／鍵盤）時原生會再推一次。 */
 (function () {
 try {
 if (!window.CubeLVSafeArea || !window.CubeLVSafeArea.getInsets) return;
 var v = JSON.parse(window.CubeLVSafeArea.getInsets());
 var s = document.documentElement.style;
 s.setProperty('--native-inset-top', v.top + 'px');
 s.setProperty('--native-inset-right', v.right + 'px');
 s.setProperty('--native-inset-bottom', v.bottom + 'px');
 s.setProperty('--native-inset-left', v.left + 'px');
 } catch (e) { /* 沒有原生介面（web / iOS）就靠 env() */ }
 })();

 (function(){if(location.pathname.indexOf('/share/')===0)return;["/assets/AICompanyPlugin-578e0aea.js","/assets/registerPluginLocales-fce228e5.js","/assets/SYSTEM_FLOW-ccbd6204.js","/assets/Plugin-a772c59b.js","/assets/AICompanyRoom-e7cc77fa.js","/assets/agentSchema-87e501d4.js","/assets/aiCompanyFolderSchema-a50e9b3e.js","/assets/mailSchema-bb484ae3.js","/assets/agentSkillSchema-3dae6627.js","/assets/mcpServerSchema-7579cf39.js","/assets/submissionSchema-12c1eb53.js","/assets/aiCompanySectionConfigSchema-d80757c8.js","/assets/systemFlowSchema-b0eb17c2.js","/assets/SubmissionInbox-980c1cba.js","/assets/SubmissionTargetPreview-65a3608e.js","/assets/SkillLibraryList-1a93a5fa.js","/assets/SkillLibraryEditor-0b4726d1.js","/assets/McpLibraryList-07ae9403.js","/assets/McpLibraryEditor-dd2ce404.js","/assets/AICompanySidebarSettings-ec82743f.js","/assets/aiCompanySectionConfigStore-c7dc0a2f.js","/assets/submissionStore-13b6863b.js","/assets/SystemFlowWorkspace-13c8d165.js","/assets/systemFlowPreview-3860e8e9.js","/assets/aiPreviewStore-f2902f8f.js","/assets/embedRendererRegistry-1fd35ebd.js","/assets/itemQueries-5710f7c1.js","/assets/AICompanyFolderDialog-310d0ad0.js","/assets/SystemFlowCanvas-c15b68bf.js","/assets/resolve-uri.umd-cf203988.js","/assets/pluginSDK-c7d1af27.js","/assets/index-03b65881.js","/assets/pluginScreenTargets-1db45073.js","/assets/DeviceFrame-9a09b8f3.js","/assets/FloatingActionButton-92eb550e.js","/assets/fabSuppressStore-72cec235.js","/assets/AiDataPreviewPanel-6ea66389.js","/assets/Workspace-74ab805e.js","/assets/WorkspaceRoot-97e354f9.js","/assets/WorkspaceSplit-732d8405.js","/assets/WorkspaceParent-84ebb88c.js","/assets/WorkspaceItem-34e8f9c9.js","/assets/WorkspaceSidedock-e1506d9c.js","/assets/WorkspaceTabs-c1cb6984.js","/assets/WorkspaceLeaf-7e10c84d.js","/assets/ViewRegistry-14e73d4b.js","/assets/PluginManager-19e136a5.js","/assets/serializer-93d29285.js","/assets/CustomHint-f15ae2d0.js","/assets/systemFlowExport-e3e62a81.js","/assets/downloadFile-94407df4.js","/assets/logo-e6b6d9fc.js","/assets/systemFlowGeneration-62828f94.js","/assets/pluginDataScope-40f76158.js","/assets/agentContentHash-4536c12a.js","/assets/personProvider-192e513d.js","/assets/MembersInfoStore-be013ce7.js","/assets/personLabelStore-6fe464b2.js","/assets/systemFlowEdges-431158d3.js","/assets/SystemFlowNodeSpecDialog-32f03532.js","/assets/dialog-5ba89e05.js","/assets/index-c955ce1e.js","/assets/index-90b75cef.js","/assets/index-f554e1d3.js","/assets/index-97c82b8a.js","/assets/index-3f418973.js","/assets/index-2fcd3928.js","/assets/index-cc0c19ec.js","/assets/index-17fae3d1.js","/assets/textarea-d3371ab5.js","/assets/ime-6eb54f3c.js","/assets/useAutosizeTextarea-b492ed9a.js","/assets/layoutBatch-c5500349.js","/assets/askCeo-da7064cd.js","/assets/sessionModelStore-780771f9.js","/assets/modelConfig-bcbf7520.js","/assets/toolIntentLabel-3879cec1.js","/assets/newFolderStore-5cb1054d.js","/assets/newContentPresentationStore-620e2a6b.js","/assets/aiCommanderSectionConfigStore-701d4f67.js","/assets/aiCommanderSectionConfigSchema-6a5ea7d7.js","/assets/useMemberSocketStore-b77fd090.js","/assets/chatRoomFolders-9146d4db.js","/assets/subscriptionConnections-e3c521da.js","/assets/index-50f51641.js","/assets/AgentExecToast-ab0a7fac.js","/assets/schema-7a6b420d.js","/assets/historySnapshotRecovery-eb4fee33.js","/assets/siteAPI-36aba80d.js","/assets/sitePublishCardRules-dab50a0f.js","/assets/sitePreviewStore-01fb66c1.js","/assets/unreadItems-0fda40f1.js","/assets/systemFlowActivity-2336f14a.js","/assets/systemFlowGhostStacks-0c378f76.js","/assets/systemFlowJourney-bea4e930.js","/assets/shareCampaignAttention-76cb90a2.js","/assets/hintStore-33a241a2.js","/assets/patchStore-cca5172c.js","/assets/backgroundTasks-007292e6.js","/assets/pushApi-2521783b.js","/assets/defaultFolderDialog-b61c38b9.js","/assets/NameInputDialog-bfe62e66.js","/assets/input-e62984e7.js","/assets/editorExtensionRegistry-2d3cf45a.js","/assets/ItemEmbedExtension-902c27ab.js","/assets/index-ea6ad0ae.js","/assets/index-a79a2195.js","/assets/index-5a0a3f44.js","/assets/index-3036054b.js","/assets/embedNavigate-d45ebf26.js","/assets/embedInstallPrompt-2e165003.js","/assets/publicEmbedRuntimeBridge-9b23a6d7.js","/assets/publicPluginRuntimeState-22cfc8a4.js","/assets/useEmbedTarget-5aa40769.js","/assets/embedRef-1c3f13a0.js","/assets/detachedEmbedItem-fd177e96.js","/assets/UnifiedSkeleton-2bd67692.js","/assets/EmbedCard-eaea742e.js","/assets/embedSnapshot-c3b89192.js","/assets/artifactSurface-b2fd6bd1.js","/assets/NoteChartExtension-d2be38e7.js","/assets/NoteChartBlock-fab90afb.js","/assets/dragStore-d1e2bf7d.js","/assets/NoteChartRender-c4aa76f8.js","/assets/exportNoteChartCsv-c135b97f.js","/assets/openExternal-a00f2b10.js","/assets/noteChartPalette-c75d91ac.js","/assets/AreaChart-0958b37a.js","/assets/noteChart-b30322ad.js","/assets/MentionPillLinkExtension-106d078f.js","/assets/MentionPillIcon-d7413217.js","/assets/icon_round_empty_24-3b5f440f.js","/assets/icon_round_checked_24-3cb79355.js","/assets/wrench-acdfd365.js","/assets/folderMenuRegistry-48931cc9.js","/assets/pluginRootRegistry-188a80d5.js","/assets/chatExtensionRegistry-a018c155.js","/assets/notificationRegistry-dc0dc7ef.js","/assets/osNotificationPermission-83a12f5c.js","/assets/PushPermissionFirstRunDialog-882df709.js","/assets/useLongPressDrag-3c13346e.js","/assets/AgentDetailPanel-1cc32034.js","/assets/tabs-de2b95c1.js","/assets/index-66563350.js","/assets/index-23adc70e.js","/assets/index-98ccf748.js","/assets/IconPicker-60f8415e.js","/assets/AgentPersonaTab-74df056d.js","/assets/creditsError-8082eb90.js","/assets/promptHost-a5d8c4f9.js","/assets/CustomScrollbar-246e607e.js","/assets/EditorFocusConfirmButton-2268748f.js","/assets/subtaskInputFocusStore-5d2f6cb1.js","/assets/MarkdownEditor-03167e31.js","/assets/index-acda34b7.js","/assets/NoteEditorToolbar-4ed993c7.js","/assets/TableSizeSelector-c005a188.js","/assets/MarkdownClipboard-af87387d.js","/assets/mdConverter-2812b4ba.js","/assets/index-47e3efb7.js","/assets/CodeBlockCopy-855f8b7b.js","/assets/ImageExtension-8d6a1fd0.js","/assets/imageTextRecognition-67310ccf.js","/assets/pluginMedia-461acc89.js","/assets/geocode-cc2eab89.js","/assets/imageDisplayUrl-84503f04.js","/assets/DeletedFilePlaceholder-84952ddb.js","/assets/VideoExtension-06410df6.js","/assets/chatAttachmentMedia-17a3d0e0.js","/assets/FileAttachmentExtension-c982452b.js","/assets/useStorageUsage-77225e3b.js","/assets/ImagePreviewWindow-a78bf0ef.js","/assets/AddUrlDialog-91f322e4.js","/assets/SearchDialog-5b15ab46.js","/assets/NoteItem-4ed993c7.js","/assets/BasicComponents-9c6af72c.js","/assets/FolderTreeSelect-4497f6b6.js","/assets/DragContext-7546ee2a.js","/assets/sidebarDropStore-e805e5a0.js","/assets/GenericFolderTreeSection-4c6e4524.js","/assets/FolderItem-ec845c9d.js","/assets/ShareMemberThumbnailList-1f02bf29.js","/assets/LetterAvatar-2fe3ea8d.js","/assets/useFolderTouchDrag-3884e106.js","/assets/customSections-776c29c2.js","/assets/customSectionOrder-e279a219.js","/assets/virtualFolderName-6c514b05.js","/assets/FolderGroup-4afdeae2.js","/assets/useUnreadAncestorIds-c3c5384b.js","/assets/useFolderGroupTree-62f2af59.js","/assets/DashedBoxAddBtn-0abdc1c6.js","/assets/DragOverlay-b0c937cd.js","/assets/AudioPlayer-ac8d014b.js","/assets/DatePickerDropdown-b10e687a.js","/assets/calendar-c82ddb47.js","/assets/calendar-8f2a03e9.js","/assets/chevron-left-d658f650.js","/assets/chevron-right-b56ad3bc.js","/assets/TimePickerDialog-a0b74ed5.js","/assets/clock-679b864d.js","/assets/DateDialog-76a500e6.js","/assets/time-picker-816c10bc.js","/assets/select-0658b858.js","/assets/index-d203b311.js","/assets/index-9be1410e.js","/assets/index-4a9f9d88.js","/assets/index-4b676365.js","/assets/index-ec40bc24.js","/assets/DateRangeDialog-22269d56.js","/assets/dateFormat-8ff7a7ca.js","/assets/toggle-group-4a5aef7f.js","/assets/toggle-b00a764a.js","/assets/icon_folder_outline_24-1a4bf83d.js","/assets/NoteEditorMenu-c1129992.js","/assets/NoteEditorMenu-4ed993c7.js","/assets/useEditorViewReady-bbedcb2e.js","/assets/SearchReplaceDialog-60dcbe9f.js","/assets/AddMenu-a37e01ec.js","/assets/ListUtils-b4ea1896.js","/assets/WebPreviewDecoration-b36e06e3.js","/assets/useWhyDidYouUpdate-62d2019e.js","/assets/IndentExtension-ccbf7666.js","/assets/DragHandleExtension-1588d244.js","/assets/TableDragHandleExtension-ed618836.js","/assets/CustomKeyboardShortcuts-c7a82566.js","/assets/NoteEditorColorUtils-71725f7b.js","/assets/RewriteHighlight-988a8a6d.js","/assets/ColorSelectionHighlight-c69807fb.js","/assets/MarkdownAutoFormatUndo-1db68b74.js","/assets/TaskItemDashInputRule-c33fb67f.js","/assets/HistoryManager-8a5645b6.js","/assets/useAIProcessing-c14ae962.js","/assets/useLinkHandler-e307482e.js","/assets/todoStore-02a94761.js","/assets/reminderTimeUtils-183a87c9.js","/assets/todoSchema-33d7910d.js","/assets/noteSchema-ff04ad79.js","/assets/useMentionSuggestion-4a627974.js","/assets/mentionSuggestions-9dee3914.js","/assets/textUtils-cfdb5232.js","/assets/MentionSuggestionList-329c02ec.js","/assets/NoteEditorToolbar-a7a437f2.js","/assets/keyboardAvoidancePolicy-e4264b83.js","/assets/TitleEditor-b91f787e.js","/assets/AgentFlowEdgesSection-ac01575e.js","/assets/switch-1e76405c.js","/assets/popover-a8e7ebe3.js","/assets/AgentSettingsTab-1b4eff45.js","/assets/modelStore-fb7e2f9c.js","/assets/userPlan-200acc44.js","/assets/premiumModelWarning-afb3b758.js","/assets/agentScheduleWeekdays-c55f988e.js","/assets/agentScheduleLabels-3071fab1.js","/assets/agentScheduleStatus-80c42226.js","/assets/deepseekPeak-7abfdf3a.js","/assets/agentModelPolicy-d48a39f9.js","/assets/AgentDeliverySettings-97865264.js","/assets/channelAPI-760795c2.js","/assets/PillPicker-01fbbc78.js","/assets/AgentDashboardTab-ae6d762d.js","/assets/AgentBudgetTab-e5f31217.js","/assets/AgentSkillsTab-76df87a0.js","/assets/SkillLibraryDialog-89986614.js","/assets/SkillEditDialog-19a23c57.js","/assets/skillApi-9058b8cc.js","/assets/cliWorkerApi-a62b7f8a.js","/assets/SkillSourceBadge-48d1e13c.js","/assets/label-1f54210c.js","/assets/SkillSearchDialog-d8754c11.js","/assets/checkbox-a1bab6ab.js","/assets/McpLibraryDialog-033bd7fc.js","/assets/McpEditDialog-204c46ab.js","/assets/McpSearchDialog-e5665523.js","/assets/McpSourceBadge-c8e99f79.js","/assets/AgentMemoryTab-29e70b21.js","/assets/agentLoginNotice-fdae53a1.js","/assets/AgentRunList-5995dd6b.js","/assets/agentRunsAPI-8b90c89c.js","/assets/AIChatBotService-e6c6a8c1.js","/assets/AICommanderChatRoom-fcbad16f.js","/assets/toolIconMap-7f3321ef.js","/assets/icon_photo_24-3662adf5.js","/assets/icon_local_computer_24-64f10b2d.js","/assets/CEOSettingsDialog-56ce2b0a.js","/assets/ChannelBindingsSection-93915129.js","/assets/icon_plug_24-c8eff703.js","/assets/AgentTaskList-c56ef106.js","/assets/SitePagePreview-1fdc71d7.js","/assets/goneReason-7a2fa76c.js","/assets/previewNavigation-2438e471.js","/assets/SiteStage-5cc0fcde.js","/assets/PluginTopbar-11d61599.js","/assets/folderActionButtons-62525f69.js","/assets/useOpenSidebar-6c20c25d.js","/assets/useImmersiveView-05a15b2e.js","/assets/useCurrentPluginDir-679720c6.js","/assets/siteEmbedTargets-9d2c9f2b.js","/assets/ArtifactView-c472c5f8.js","/assets/artifactSanitize-c3714dc0.js","/assets/siteStatus-08d64b7f.js","/assets/pendingChanges-eef364cd.js","/assets/lastLayoutEdit-d7e30372.js","/assets/ChatMessageAssistant-5e7539d8.js","/assets/WidgetExtension-af2b9509.js","/assets/SitePublishAction-1639d0cb.js","/assets/onboardingFirstRunNavigation-a4886c8a.js","/assets/UsageLimitNotice-c8cadf3a.js","/assets/subscriptionOffer-2bfa6efa.js","/assets/TurnLimitNotice-9459267a.js","/assets/SubagentCard-830e2f32.js","/assets/subagentView-491b2923.js","/assets/SubagentPanel-280689c7.js","/assets/SessionOutputBar-d79c83f6.js","/assets/LoopLimitNotice-08a26167.js","/assets/ForgeCard-9c6e7327.js","/assets/SubscriptionFallbackCard-797c4972.js","/assets/AskUserQuestionPanel-281cc334.js","/assets/AICommanderChatRoomTopbarTitle-3755ade4.js","/assets/LiveBrowserView-1300b54b.js","/assets/LiveViewShell-2e377770.js","/assets/ExecutorBadge-b138bc7e.js","/assets/mobileLocalBrowser-be44987b.js","/assets/MobileBrowserLogin-443adef3.js","/assets/BrowserAuthRequestCard-48dd8d48.js","/assets/ChatInputArea-4fb74bd6.js","/assets/ComposerEditor-987d08f4.js","/assets/hydrateMentionIcons-8f6fff40.js","/assets/useChatComposer-4383eca3.js","/assets/icon_audio_on_26-841d8a80.js","/assets/VoiceDictationBar-b5ce2cd9.js","/assets/icon_stop_round_26-8cb04168.js","/assets/round_send_26_n-f8de8c5e.js","/assets/sendContext-512fec7b.js","/assets/ChatModelSelector-89a8e1dd.js","/assets/ChatImagePicker-f167fa96.js","/assets/ChatSendStopButton-50225149.js","/assets/ChatPreInputQueue-f21c8139.js","/assets/ChatDriveAuthorizationCard-3451d978.js","/assets/driveAuthGateStore-26816d57.js","/assets/googleDriveAuthGate-57637b8c.js","/assets/googleDriveLinks-911ef564.js","/assets/ChatMobileAddMenu-cf5bc523.js","/assets/icon_ai_chat_24-47b856f9.js","/assets/icon_check-2dba3d0e.js","/assets/subscriptionConnectionsStore-011aaa93.js","/assets/ChatEffortSelector-85a0820a.js","/assets/MessageAttachment-948a8de7.js","/assets/ChatImageDropZone-92ddea18.js","/assets/DeleteAgentConfirmDialog-c64becb2.js","/assets/folderShareHandler-2a1a9989.js","/assets/publicItemTypeRegistry-85e82de8.js","/assets/MarkupMenuButton-6188584f.js","/assets/agentStore-d4c35ca0.js","/assets/useSidebarSwipeGesture-68e44329.js","/assets/swipeSuppressStore-66d1e715.js","/assets/NewContentPresentationRow-ae60e7b5.js","/assets/useMarkListItemsRead-242a5918.js","/assets/SubmissionSettingsDialog-04ac2df1.js","/assets/formatTimeAgo-8d224ad7.js","/assets/SubmissionPanel-be3c677d.js","/assets/GoalPickerDialog-6a356ee2.js","/assets/goalCandidates-13ee8dbc.js","/assets/icon_sliders_24-194eb0cb.js","/assets/systemFlowJourneyActivity-0e9adf1f.js","/assets/CardGalleryPlugin-230dba45.js","/assets/CardGallery-0ca4ad65.js","/assets/AddCardTemplateDialog-4a7dfa0d.js","/assets/cardStore-4b0cf6bb.js","/assets/cardSchema-f2de2f12.js","/assets/cardFieldUtils-f0e35ff4.js","/assets/cardAI-d02f6e00.js","/assets/promptClient-11ca5676.js","/assets/CardRenderer-8677e63f.js","/assets/commentStore-8735c853.js","/assets/commentApi-787cf5b0.js","/assets/cardHtml-e640e4d9.js","/assets/menuStore-9d84371f.js","/assets/useScrollToFocusedItem-5a7f0a04.js","/assets/GuestFavoriteButton-7fa351c6.js","/assets/icon_close-09c69eea.js","/assets/LazyCard-4cfcaf36.js","/assets/AvatarWithBubble-13a297c2.js","/assets/EditHistoryPanel-7601fe23.js","/assets/EditHistoryList-204ae1e3.js","/assets/goLinkAPI-7644997f.js","/assets/CardListView-ece4e469.js","/assets/NoEditPermissionDialog-19b54674.js","/assets/CardGalleryMapView-bedfe331.js","/assets/geolocation-b4ff52bc.js","/assets/CardPreviewDialog-bb353465.js","/assets/CommentsListDialog-1a88a241.js","/assets/AddCardDialog-fb977b3e.js","/assets/icon_star_empty_24-d047c558.js","/assets/icon_star_full_24-9c5bf665.js","/assets/DeleteCardConfirmDialog-9b8a438b.js","/assets/EditTemplateDialog-dc057989.js","/assets/WriteCommentDialog-7284bdaf.js","/assets/cardGalleryLayout-96a2011b.js","/assets/target-8a1cd9fd.js","/assets/EditorPlugin-fe7dc33c.js","/assets/NoteEditor-141f72b9.js","/assets/NoteEditorTopbar-fd8a9e64.js","/assets/recordingManager-9197e1e7.js","/assets/noteAudioFolder-3330a490.js","/assets/storageQuota-347ddde6.js","/assets/prompts-05389b79.js","/assets/downloadNote-3f894bdd.js","/assets/pdf-82e26b48.js","/assets/PostComposer-a64e1b7a.js","/assets/postFolders-5ed8f2bb.js","/assets/wallPostTemplate-3d54817f.js","/assets/wallPublishRun-cbf469e5.js","/assets/wallStore-7fbfe1ce.js","/assets/wallApi-84353ae0.js","/assets/postEmbedRenders-8152ba05.js","/assets/embedCapture-1bff233b.js","/assets/EmbedPickerDialog-831ffc12.js","/assets/embedResolve-162d4f0e.js","/assets/NotePickerDialog-0a4427dd.js","/assets/PublishNoteDialog-1863b4e5.js","/assets/music-7c988ca2.js","/assets/SetReminderTimeDialog-2e731111.js","/assets/EditNoteTagDialog-e9d1a259.js","/assets/ConvertToSubtaskDialog-8df31b75.js","/assets/PermanentItemDeleteConfirmDialog-ec5aef0b.js","/assets/deleteConfirmation-160d3e9e.js","/assets/NoteLeaveSharedConfirmDialog-b5098ab9.js","/assets/NoteEditorTitle-b25d2dc7.js","/assets/TodoCheckbox-5c41beae.js","/assets/NoteEditorMetaBar-bb158071.js","/assets/editorAI-428aa71e.js","/assets/prompts-f23fe025.js","/assets/CustomMetaBar-4da9dcf6.js","/assets/TodoTaskBar-0d980422.js","/assets/AssigneeAvatar-20f849d4.js","/assets/UserAvatar-9dcb8c4c.js","/assets/AssigneePicker-f79e2a4a.js","/assets/icon_calendar_outline_24-a509cee5.js","/assets/TodoItem-4ed993c7.js","/assets/TodoParentBreadcrumb-6f68d1b7.js","/assets/TodoList-7ab3c43a.js","/assets/Sidebar-4ed993c7.js","/assets/TodoItem-cc6adf1a.js","/assets/flag-cc649611.js","/assets/todoSectionConfigStore-fb905129.js","/assets/todoSectionConfigSchema-9e357ff7.js","/assets/TodoRightClickMenu-b4554d9a.js","/assets/leaveCheckGuard-08447c1e.js","/assets/TodayTimeline-c548d17d.js","/assets/eventStore-2b501c78.js","/assets/calendarSchema-ed80615f.js","/assets/calendarPrefs-f9c251f5.js","/assets/eventSchema-2cd75433.js","/assets/recurrenceUtils-247ccd63.js","/assets/EventDialog-e5e00133.js","/assets/DayEntryRow-1334b20e.js","/assets/artifactRepair-80cf2a03.js","/assets/artifactEmbeds-5df902fa.js","/assets/artifactImages-e324729b.js","/assets/artifactCreate-10a324ef.js","/assets/useFileInsert-8d363292.js","/assets/uploadDedup-76211950.js","/assets/noteFilesFolder-cc5857da.js","/assets/fileKind-ce30ff67.js","/assets/noteEmbedInsert-f1bf918e.js","/assets/ArtifactCreditDialog-1574a90e.js","/assets/artifactSync-1a595209.js","/assets/AudioContainer-50c3dd90.js","/assets/useAudioRecording-49c7847d.js","/assets/AudioPlayer-8edb3b2a.js","/assets/AudioTranscriptDialog-3a941e1f.js","/assets/AudioRecorder-9c86b8b3.js","/assets/CommentThread-04f8d0ec.js","/assets/ReportDialog-10105d52.js","/assets/renderMentions-9ddcbc02.js","/assets/openCommunityProfile-669b4abf.js","/assets/chatRoomStore-14489bdb.js","/assets/dropdown-menu-f43a7d7a.js","/assets/index-c050e965.js","/assets/heart-7f706750.js","/assets/EditorPlaceholder-1727e328.js","/assets/SettingDialog-21ac4ad5.js","/assets/EditorErrorBoundary-ab577bde.js","/assets/useImageUpload-0211bd39.js","/assets/noteImagesFolder-9f900ec9.js","/assets/useWebsitePreview-b68711aa.js","/assets/useNoteActions-d0684437.js","/assets/useEditorKeyboard-e53e09f4.js","/assets/artifactSubscriptionPrompt-5102d6e8.js","/assets/JointCompanyLockedPlugin-ac5289dd.js","/assets/JointCompanyPaywall-3da56dff.js","/assets/NoteListPlugin-4c5da2a7.js","/assets/NoteList-d4013330.js","/assets/NoteRightClickMenu-f485d973.js","/assets/NoteItem-e2e84f1d.js","/assets/NoteListTopbar-90e1938b.js","/assets/noteImport-4355fb5f.js","/assets/NoteListToolBar-c0e15608.js","/assets/EditFolderSummaryDialog-bc649466.js","/assets/SitePlugin-bdca982a.js","/assets/siteSchema-a1aff61f.js","/assets/SiteListView-13f1fbdb.js","/assets/SiteRenderView-84808fae.js","/assets/TodoPlugin-6e7c4dcb.js","/assets/TODO-cce9ba4e.js","/assets/TodoSidebarSettings-c88b816c.js","/assets/TodoEditorView-66cef92c.js","/assets/CalendarView-cc30f6ea.js","/assets/TodoFolderDialog-2caa4248.js","/assets/TodoEmbedView-210bd433.js","/assets/CalendarLegend-2dd3ec09.js","/assets/MonthYearPicker-ce271bf9.js","/assets/lunar-272a6ef2.js","/assets/monthLayout-ca9be618.js","/assets/DayDetailPanel-5ccb61cd.js","/assets/TodoDetailPanel-335d2ad2.js","/assets/dayPanelNavigation-244497eb.js","/assets/weekCellSelection-8c1cc3ae.js","/assets/CalendarWidgetGuideDialog-f55bb047.js","/assets/calendarConnectionRoute-b618a826.js","/assets/TrashPlugin-d210ef13.js","/assets/TrashList-d0b68cd5.js","/assets/TrashPreview-2cf7e79c.js","/assets/ClearTrashDialog-585dbff0.js","/assets/trashDelete-b4a96d74.js","/assets/trashRoot-0e27d2ca.js","/assets/NotePlugin-73191509.js","/assets/NOTE-93f6e85a.js","/assets/noteSectionConfigSchema-01ff7659.js","/assets/shareEmbedRenders-0c98d444.js","/assets/windowComponentRegistry-729586ca.js","/assets/NoteWindowContent-535d6ede.js","/assets/NoteFolderDialog-9f144010.js","/assets/NoteEmbedView-a41aae1d.js","/assets/AppConfigPlugin-f4c30e97.js","/assets/AICommanderPlugin-90ecfd3f.js","/assets/AICommander-de0ad218.js","/assets/AiCenterContent-183001d5.js","/assets/SessionSearchDialog-4342b8bf.js","/assets/OnboardingTeamDialog-6f8599d0.js","/assets/OnboardingWelcomeDialog-d17ca822.js","/assets/AICommanderFab-d07ca8df.js","/assets/OnboardingTeamDialog-4ed993c7.js","/assets/AICommander-4ed993c7.js","/assets/AICommanderHistory-33d73f08.js","/assets/useSessionContextMenu-384186ff.js","/assets/useSessionContentSearch-8332b43c.js","/assets/AICommanderHistorySection-fa26d174.js","/assets/onboardingFixedPathStart-19ff1787.js","/assets/onboardingModelAccess-e16f9183.js","/assets/parseHoldingsScreenshot-d011cd9c.js","/assets/marketData-aee0865f.js","/assets/holdings-1166c777.js","/assets/CardPlugin-58cea765.js","/assets/CARD-c7b7b84f.js","/assets/cardEmbedSampleItems-24aa41bc.js","/assets/cardSectionConfigSchema-03362a5f.js","/assets/CardRecognitionHint-8645b499.js","/assets/CardTemplateDialog-6b5b96b9.js","/assets/CardWindowContent-477c1f63.js","/assets/PermissionNotificationItem-139f2209.js","/assets/CardEmbedView-a7da79af.js","/assets/CardEmbedDisplay-ee9160ce.js","/assets/progress-65fae53c.js","/assets/ChatPlugin-d88de2c5.js","/assets/chatRoomFolderSchema-d602c863.js","/assets/pollSchema-81b3d2b0.js","/assets/ChatRoomView-be13ac9c.js","/assets/CreateRoomDialog-21bf5763.js","/assets/ChatRoomLeaveConfirmDialog-6a60475f.js","/assets/DirectMessageDeleteConfirmDialog-a19720e2.js","/assets/trophy-edba04a6.js","/assets/RoomPoll-a38263fd.js","/assets/roomPoll-d89ec807.js","/assets/LinkifiedText-b3cb2863.js","/assets/UrlPreviewCard-42fb34f3.js","/assets/openDirectMessage-1514c49c.js","/assets/RoomPostPickerDialog-343b810a.js","/assets/RoomPostQuoteCard-8f1ed0a3.js","/assets/PostCard-f21c20b0.js","/assets/share-da5ff46f.js","/assets/PostRepliesPanel-2a79dd8b.js","/assets/liveEmbedLease-9528ee11.js","/assets/message-circle-46c3ef3b.js","/assets/send-bec70674.js","/assets/RoomEmbedCard-c71086b0.js","/assets/embedSource-125b1b6a.js","/assets/openMarketplaceListing-1431195c.js","/assets/marketplaceStore-9b837e87.js","/assets/marketplaceRequestCache-d9c3b300.js","/assets/systemFolders-bced443e.js","/assets/jointCompanyStore-fc575311.js","/assets/jointCompanyApi-edac3ea3.js","/assets/JointCompanyChannelWindow-ee197ee3.js","/assets/jointCompanyChannelStore-d8f8df70.js","/assets/jointCompanyNavigation-d76dacf1.js","/assets/JoinJointCompanyDialog-7b32722d.js","/assets/JointCompanyPaywallDialog-3e3261de.js","/assets/embedAttachments-5c075a36.js","/assets/JointCompanyPlugin-aee946a1.js","/assets/jointCompanySchema-3d149a51.js","/assets/FileLibraryPlugin-81a0f223.js","/assets/fileSchema-92accf8f.js","/assets/FileGrid-a330c848.js","/assets/FileMetadataPane-8800a039.js","/assets/fileVisibility-a830130f.js","/assets/fileCacheStore-1ec5542c.js","/assets/fileViewStore-18f1609d.js","/assets/FileGridItem-695ceff0.js","/assets/openFile-27c20fbe.js","/assets/cloud-download-2b7ca758.js","/assets/FileRightClickMenu-893e3bea.js","/assets/FileRenameDialog-9a3ec7c8.js","/assets/VideoPreviewWindow-8dc4f51e.js","/assets/FileLibraryUsageBar-a641f201.js","/assets/file-plus-a4ece329.js","/assets/PlaceholderPlugin-57df2ac3.js","/assets/PlaceholderView-56bf3e29.js","/assets/MaterialLibraryPlugin-c08e33ac.js","/assets/MaterialLibrary-2696ad54.js","/assets/MaterialLibraryListItem-c5105294.js","/assets/MaterialLibraryHistoryItem-e61a6cf8.js","/assets/noteSectionConfigStore-ee76327c.js","/assets/MailboxPlugin-dd79941e.js","/assets/mailFolderSchema-cc026cc6.js","/assets/MailList-bd84f259.js","/assets/MailReader-8984b12b.js","/assets/mailStore-a3910419.js","/assets/useCurrentMailFolderID-f4ccc280.js","/assets/MailHtmlBody-4c2717fa.js","/assets/reply-02dea615.js","/assets/forward-4a29d4ef.js","/assets/CommunityPlugin-73050942.js","/assets/communitySchema-0d17edc7.js","/assets/postSchema-a096ecde.js","/assets/ProfileView-d175ea5b.js","/assets/WallView-09e24637.js","/assets/PostDetailPage-7a162cf9.js","/assets/NewListingNotificationItem-d91dd4e0.js","/assets/MarketplaceReviewNotificationItem-b032b7db.js","/assets/ShareItemViewerDialog-2381402d.js","/assets/ReplyNotificationItem-2392f883.js","/assets/NewPostNotificationItem-8a48ee29.js","/assets/marketplaceSchema-59ff5af9.js","/assets/MarketplaceList-a0888895.js","/assets/MarketplaceDetail-8aeea727.js","/assets/MarketplaceListingDialog-ff21acb9.js","/assets/MarketplaceAcquireDialog-f613faeb.js","/assets/MarketplaceSubscriptionsDialog-fad5555a.js","/assets/MarketplaceSellDialog-2307027f.js","/assets/ja-d5646942.js","/assets/communityApi-7118f9d0.js","/assets/FollowListDialog-2f84c933.js","/assets/CommunitySearchView-30ead1d0.js","/assets/MarketplaceRatingStars-bd1fe4cb.js","/assets/marketplaceReviewStore-e593881f.js","/assets/MarketplaceVideo-df26052b.js","/assets/x-bd88c345.js","/assets/ticket-f0b678dd.js","/assets/useScrolledArticle-14fce4c4.js","/assets/PullToRefresh-c3946876.js","/assets/LogoSpinner-d80dae16.js","/assets/SlideCanvas-fe1cdd91.js","/assets/apiError-92110813.js","/assets/SlideRuntime-99609fe9.js","/assets/locTags-702ec2ec.js","/assets/babelWalk-2094f58c.js","/assets/SlideErrorBoundary-3f56a63e.js","/assets/slideDesign-ab895763.js","/assets/snapshot-c52a73d1.js","/assets/SlideSurface-e6272be8.js","/assets/ownerPlanWatermark-9433033e.js","/assets/MarketplaceContentUpdateDialog-d3b0ece7.js","/assets/pluginEmbedPreview-b8dfb853.js","/assets/pluginLoader-d2c9ef26.js","/assets/marketplaceReviewPolling-4b95e49c.js","/assets/MarketplaceReviewList-9a4e888f.js","/assets/MarketplaceRatingSummary-8eb4dc0e.js","/assets/MarketplaceWriteReviewDialog-6524cd3b.js","/assets/MarketplaceSellerReplyDialog-45176e46.js","/assets/thumbs-up-b1dde156.js","/assets/play-cefe71ad.js","/assets/MarketplaceSubcategoryTags-f1a02e6a.js","/assets/video-13a01542.js","/assets/image-plus-f064fa32.js","/assets/packageInstallFlow-fb045136.js","/assets/MarketplaceSubscriptionsPanel-f0971ed0.js","/assets/SlidePlugin-6401a2d4.js","/assets/slideStore-23dfc9be.js","/assets/slideSchema-d8e04d6b.js","/assets/slideSectionConfigSchema-1b898e9e.js","/assets/SlideList-c1e5f1a3.js","/assets/SlideEditor-6b6bc6c1.js","/assets/SlideWindowContent-e040b417.js","/assets/SlideFolderDialog-5904205d.js","/assets/SlideDesignPanel-d596e059.js","/assets/slider-72840e4e.js","/assets/sparkles-64de801a.js","/assets/SlideInspectorPanel-3c08d360.js","/assets/bold-2d793f02.js","/assets/italic-322fcf31.js","/assets/text-align-start-c187eb71.js","/assets/text-align-center-1eeb5c7a.js","/assets/text-align-end-ff89feb8.js","/assets/text-align-justify-d93a5ce1.js","/assets/SlidePresent-a989848d.js","/assets/SlidePresenterView-78614e7b.js","/assets/pointer-c0787217.js","/assets/square-check-eb67c264.js","/assets/monitor-8f04c408.js","/assets/circle-question-mark-4dd9f6b0.js","/assets/slideExport-9596f24d.js","/assets/slideExportDocument-26fcf59f.js","/assets/editOps-92f95d31.js","/assets/circle-play-1650c079.js","/assets/scan-eye-65133e89.js","/assets/palette-bd88e4d6.js","/assets/SidebarPlugin-17eb3c65.js","/assets/sidebarDrop-a9d0d2aa.js","/assets/SidebarFolderContextMenu-42031063.js","/assets/computeIsGroup-371f76e9.js","/assets/Sidebar-ea4bdcc5.js","/assets/SuggestionDialog-bf34bc7e.js","/assets/RateAppDialog-ce193ac9.js","/assets/RewardTasksDialog-c12228be.js","/assets/JoinSharedItemDialog-375a3eb2.js","/assets/GenericFolderDeleteConfirmDialog-6155cfad.js","/assets/GroupRenameDialog-a1ec3588.js","/assets/AddToHomeScreenGuideDialog-96746353.js","/assets/FolderWidgetSetupDialog-29efbad6.js","/assets/icon_upgrade_24-e35b5d6f.js","/assets/ConnectionStatusDot-1df72a67.js","/assets/LottieAnimation-5a023e70.js","/assets/SidebarTopbar-e42c9504.js","/assets/InappNotificationBell-49ce6b23.js","/assets/inappNotificationStore-7c99481b.js","/assets/notificationRouter-9a33ad89.js","/assets/pluginReconciler-53f93db1.js","/assets/pluginMountQueue-2f08c13d.js","/assets/migrateLegacySectionKeys-7a041d9d.js","/assets/freezeWatchdog-6d2f3e0f.js","/assets/pluginSafeMode-8d1d0382.js","/assets/quant-62d087f7.js","/assets/InappNotificationPanel-edfff5d9.js","/assets/DefaultInappNotificationItem-f19bffb0.js","/assets/useNewFolderPresentation-339c5e2e.js","/assets/GenericSidebarSection-b7b4c673.js","/assets/CustomFunctionsSection-cf0d5998.js","/assets/CustomSection-c43661c5.js","/assets/TrashSidebarEntry-b188cddf.js","/assets/AISidebarNav-2a448323.js","/assets/LimitedOfferBanner-51abbade.js","/assets/clock-3-a23200ee.js","/assets/SubscriptionQuotaBar-ebcfca9c.js","/assets/SidebarDialogHosts-a8a01358.js","/assets/siblingGroupNames-abf619bb.js","/assets/check-d1294690.js","/assets/ClassifyPlugin-20bc7b35.js","/assets/ClassificationService-15640220.js","/assets/ClassifyHint-acc44360.js","/assets/NoteItem_ClassifyDecoration_patch-fa42279c.js","/assets/TodoItem_ClassifyDecoration_patch-57d1705d.js","/assets/noteStore_classify_patch-b95fc3b3.js","/assets/todoStore_classify_patch-d0167373.js","/assets/sidebar_classify_patch-1ce7582b.js","/assets/note_menu_classify_patch-a3938f91.js","/assets/toolbar_classify_patch-d63b3a42.js","/assets/MailItem_ClassifyDecoration_patch-e76b2954.js","/assets/mailStore_classify_patch-31a731f1.js","/assets/classifyStore-16860fec.js","/assets/classifyAI-a486a83c.js","/assets/prompts-cb1a7bf5.js","/assets/classifyUtils-a0d9144a.js"].forEach(function(h){var l=document.createElement('link');l.rel='modulepreload';l.crossOrigin='';l.href=h;document.head.appendChild(l);});})();

  

 // boot overlay 控制：React 透過這兩個函數更新同步狀態文字 / ready 後淡出（見 App.tsx）。
 window.__setBootStatus = function (t) {
 var e = document.getElementById('boot-status');
 if (e) e.textContent = (t == null || t === '') ? ' ' : t;
 };
 // 不 removeChild — 改 show/hide，讓冷啟動與登入流程共用同一套 cube（登入後 sync 也要它撐場）。
 window.__showBootOverlay = function () {
 var e = document.getElementById('boot-overlay');
 if (!e) return;
 e.__hidden = false;
 e.style.display = '';
 e.style.transition = 'none';
 e.style.opacity = '1';
 e.style.pointerEvents = '';
 };
 window.__hideBootOverlay = function () {
 var e = document.getElementById('boot-overlay');
 if (!e || e.__hidden) return;
 e.__hidden = true;
 // 啟動總耗時追蹤（輕量：boot 收掉那刻 log 一次 page load → 主畫面可見的毫秒，非每幀取樣，不吃 CPU）
 try { console.log('[BootReady] page load → 主畫面 ' + Math.round(performance.now()) + 'ms'); } catch (_) {}
 e.style.pointerEvents = 'none';
 // opacity:1 完全遮蓋時瀏覽器會跳過底下 #root 的 paint，直接淡出會露出未 paint 的白底。
 // 先降到 0.99 解除「完全遮蓋」逼底下先 paint，等 2 個 rAF 確定 paint 完，再淡出。
 e.style.opacity = '0.99';
 requestAnimationFrame(function () {
 requestAnimationFrame(function () {
 if (e.__hidden === false) return; // 淡出途中又被要求顯示就取消
 e.style.transition = 'opacity 280ms ease-out';
 e.style.opacity = '0';
 // 淡出完設 display:none 停掉 cube 動畫省 CPU；再次 show 時 cube 從頭（新 loading session）。
 setTimeout(function () { if (e.__hidden) e.style.display = 'none'; }, 320);
 });
 });
 };

 阻塞啟動。
 多數人沒開 → 完全不載，啟動少 ~270ms 阻塞。 -->

 function __mountVConsole() {
 if (window.__vConsole || typeof VConsole === 'undefined') return;
 var __vcLabel = 'vConsole 1.10.1819';
 window.__vConsole = new VConsole({
 onReady: function () {
 var sw = document.querySelector('#__vconsole .vc-switch');
 if (sw) sw.textContent = __vcLabel;
 }
 });
 if (!document.getElementById('__vconsole_position_style')) {
 var style = document.createElement('style');
 style.id = '__vconsole_position_style';
 style.textContent = '#__vconsole .vc-switch { left: max(env(safe-area-inset-left, 0px), 12px) !important; right: auto !important; bottom: max(env(safe-area-inset-bottom, 0px), 24px) !important; top: auto !important; }';
 document.head.appendChild(style);
 }
 }
 window.__cubelvInitVConsole = function () {
 if (window.__vConsole) return;
 if (typeof VConsole !== 'undefined') { __mountVConsole(); return; }
 // 動態 async 載入（不阻塞啟動），載完才 mount
 var s = document.createElement('script');
 s.src = '/vconsole.min.js';
 s.async = true;
 s.onload = __mountVConsole;
 document.head.appendChild(s);
 };
 window.__cubelvDestroyVConsole = function () {
 if (window.__vConsole) {
 window.__vConsole.destroy();
 window.__vConsole = null;
 }
 };
 // 啟動時若已啟用 → 動態 async 載入（不擋啟動）
 if (localStorage.getItem('cubelv.vConsoleEnabled') === 'true') {
 window.__cubelvInitVConsole();
 }

 // @font-face 已在 宣告，CSS engine 認識字型後 browser 在 visibility:hidden 元素存在時
 // 即開始抓字型。但 @font-face 有 lazy loading：browser 不保證 CSS engine ready 前字型已完全
 // decode 並可 render。這裡用 JS new FontFace().load()：imperative call，
 // Promise 只在字型真正可 render 時才 resolve，確保 _showMaterialIcons 後字型立即可用。
 (function() {
 var _shown = false;
 function _showMaterialIcons() {
 if (_shown) return;
 _shown = true;
 document.documentElement.classList.add('fonts-loaded');
 var style = document.createElement('style');
 style.textContent = '.material-symbols-outlined, .g-icon { visibility: visible !important; }';
 document.head.appendChild(style);
 window.dispatchEvent(new CustomEvent('material-symbols-ready'));
 }
 var face = new FontFace(
 'Material Symbols Outlined',
 "url('/fonts/MaterialSymbolsOutlined.woff2') format('woff2')",
 { style: 'normal', weight: '100 700', display: 'block' }
 );
 face.load()
 .then(function(f) { document.fonts.add(f); _showMaterialIcons(); })
 .catch(function() { _showMaterialIcons(); });
 })();

# HTML CMS Tool

## 评论（1/1）

> **DylanMerigaud** · 2026-09-24T07:41:13.000Z　
> Blueprint creation before execution is a smart design.

## 关联链接

- https://astockteam.ai
- https://astockteam.com

## 导航

- 项目页：[[10-项目/app.cubelv.com_865bece8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
