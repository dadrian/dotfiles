#!/usr/bin/env python3
import json

INVISIBLE = '#ffffff00' # white with no opacity
NONE = '#00000000'

BROWN = '#d1b897'
DARK_BROWN = '#80845e'
DARK_GREEN = '#062626'
TURQUOISE = '#40b0b0'

LIGHT_GREEN = '#8cde94'
BLACK = '#000000'

BLUE = '#0000ff'
BLUE_HIGHLIGHT = BLUE + '8e'
VISUAL = BLUE
VISUAL_HIGHLIGHT = BLUE_HIGHLIGHT

PINK = '#f9d9d9'
SEARCH = PINK

BACKGROUND = DARK_GREEN
FOREGROUND = BROWN
TEXT = BROWN
TRANSPARENT_TEXT = TEXT + '00'
STRINGS = TURQUOISE

HIGHLIGHT_GRAY = '#63878a8e'
HIGHLIGHT_GRAY_LESS = '#63878a1a'


theme = {
	"name": "dadrian",
	"type": "hc",
	"colors": {
		"activityBar.activeBackground": BACKGROUND,
		"activityBar.activeBorder": FOREGROUND,
		"activityBar.background": BACKGROUND,
		"activityBar.border": FOREGROUND, # right side of activity bar
		"activityBar.foreground": FOREGROUND, # icon color in activity bar
		"activityBarBadge.background": FOREGROUND, # inverse
		"activityBarBadge.foreground": BACKGROUND, # inverse
		"button.background": DARK_BROWN,
		"button.hoverBackground": BROWN,
		"checkbox.border": DARK_BROWN,
		"contrastBorder": DARK_BROWN,
		"debugExceptionWidget.border": FOREGROUND,
		"debugToolBar.border": FOREGROUND,
		"dropdown.background": BACKGROUND,
		"dropdown.border": FOREGROUND,
		"dropdown.listBackground": BACKGROUND,
		"editor.background": BACKGROUND,
		"editor.foreground": FOREGROUND,
		"editor.findMatchBackground": SEARCH,
		"editor.findMatchHighlightBackground": HIGHLIGHT_GRAY,
        "editor.findRangeHighlightBackground": VISUAL,
        "editor.findMatchBorder": INVISIBLE,
        "editor.findMatchHighlightBorder": INVISIBLE,
        "editor.findRangeHighlightBorder": INVISIBLE,
		"editor.lineHighlightBackground": INVISIBLE,
		"editor.lineHighlightBorder": INVISIBLE,
		"editor.selectionBackground": VISUAL,
		"editor.selectionForeground": NONE,
		"editor.selectionHighlightBackground": HIGHLIGHT_GRAY,
        "editor.selectionHighlightBorder": INVISIBLE,
		"editor.rangeHighlightBackground": HIGHLIGHT_GRAY,
        "editor.rangeHighlightBorder": INVISIBLE,
		"editorBracketHighlight.foreground1": TEXT,
		"editorBracketHighlight.foreground2": TEXT,
		"editorBracketHighlight.foreground3": TEXT,
		"editorBracketHighlight.foreground4": TEXT,
		"editorBracketHighlight.foreground5": TEXT,
		"editorBracketHighlight.foreground6": TEXT,
		"editorBracketHighlight.unexpectedBracket.foreground": "#ff0000",
		"editorBracketMatch.background": TRANSPARENT_TEXT,
		"editorBracketMatch.border": TEXT,
		"editorCursor.background": BLACK,
		"editorCursor.foreground": LIGHT_GREEN,
		"editorGroup.border": FOREGROUND,
		"editorGroup.dropBackground": HIGHLIGHT_GRAY_LESS,
        "editorGroupHeader.border": FOREGROUND,
		"editorGroupHeader.tabsBackground": BACKGROUND,
		"editorGroupHeader.noTabsBackground": BACKGROUND,
		"editorGroupHeader.noTabsBorder": FOREGROUND,
		"editorLineNumber.activeForeground": "#b59e7a",
		"editorLineNumber.foreground": "#b59e7a65",
		"editorSuggestWidget.background": "#042327",
		"editorSuggestWidget.foreground": "#cccccc",
		"editorSuggestWidget.highlightForeground": "#bdb395",
		"editorSuggestWidget.selectedBackground": "#b59e7a65",
		"focusBorder": "#ffffff00",
		"foreground": BROWN,
		"input.background": "#2a343e",
		"input.border": "#b59e7a",
		"list.activeSelectionBackground": "#b59e7a",
		"list.dropBackground": "#63878a1a",
		"list.focusBackground": "#b59e7aa4",
		"list.highlightForeground": "#bdb395",
		"list.hoverBackground": "#b59e7a65",
		"list.inactiveSelectionBackground": "#b59e7aa4",
		"menu.border": "#b59e7a",
		"menu.foreground": "#cccccc",
		"menu.selectionBackground": "#b59e7a65",
		"panel.border": "#b59e7a",
		"panelSection.dropBackground": "#63878a1a",
		"panelTitle.activeForeground": "#bdb395",
		"panelTitle.inactiveForeground": "#cccccc",
		"peekView.border": "#b59e7a",
		"peekViewEditor.background": "#0c141f",
		"peekViewEditor.matchHighlightBackground": "#63878a8e",
		"peekViewResult.background": "#0c141f",
		"peekViewResult.selectionBackground": "#b59e7a",
		"quickInputList.focusBackground": "#b59e7aa4",
		"scrollbarSlider.background": "#b59e7aa4",
		"scrollbarSlider.hoverBackground": "#b59e7a",
		"sideBar.background": "#042327",
		"sideBar.dropBackground": "#63878a1a",
		"sideBar.foreground": "#cccccc",
		"sideBarSectionHeader.background": "#b59e7a",
		"sideBarSectionHeader.foreground": "#000000",
		"sideBarTitle.foreground": "#bbbbbb",
		"statusBar.background": "#b59e7a",
		"statusBar.border": "#b59e7a",
		"statusBar.debuggingBorder": "#b59e7a",
		"statusBar.foreground": "#000000",
		"statusBar.noFolderBackground": "#b59e7a",
		"tab.activeBackground": FOREGROUND,
		"tab.activeForeground": BACKGROUND,
        "tab.activeBorder": FOREGROUND,
		"tab.border": FOREGROUND,
		"tab.hoverBackground": "#b59e7aa4",
		"tab.inactiveBackground": BACKGROUND,
		"tab.inactiveForeground": FOREGROUND,
		"tab.unfocusedActiveBackground": FOREGROUND + '65',
		"tab.unfocusedActiveForeground": BACKGROUND,
		"titleBar.activeBackground": "#052c31",
		"titleBar.border": "#b59e7a",
		"titleBar.inactiveBackground": "#0c141f",
		"window.activeBorder": "#b59e7a",
		#"activityBar.dropBorder": "#d7dae0",
		#"activityBar.inactiveForeground": "#ffffff",
		#"badge.background": "#000000",
		#"badge.foreground": "#ffffff",
		#"banner.background": "#b59e7a",
		#"banner.iconForeground": "#3794ff",
		#"breadcrumb.activeSelectionForeground": "#dcc9b0",
		#"breadcrumb.background": DARK_GREEN,
		#"breadcrumb.focusForeground": "#dcc9b0",
		#"breadcrumb.foreground": "#d1b897cc",
		#"breadcrumbPicker.background": "#0c141f",
		#"button.border": "#b59e7a",
		#"button.foreground": "#ffffff",
		#"button.secondaryForeground": "#ffffff",
		#"charts.blue": "#3794ff",
		#"charts.foreground": BROWN,
		#"charts.green": "#89d185",
		#"charts.lines": "#d1b89780",
		#"charts.orange": "#ab5a00",
		#"charts.purple": "#b180d7",
		#"checkbox.background": "#2a343e",
		#"checkbox.foreground": "#ffffff",
		#"contrastActiveBorder": "#ffffff00",
		#"debugConsole.errorForeground": "#f48771",
		#"debugConsole.infoForeground": BROWN,
		#"debugConsole.sourceForeground": BROWN,
		#"debugConsole.warningForeground": "#008000",
		#"debugConsoleInputIcon.foreground": BROWN,
		#"debugExceptionWidget.background": "#420b0d",
		#"debugIcon.breakpointCurrentStackframeForeground": "#ffcc00",
		#"debugIcon.breakpointDisabledForeground": "#848484",
		#"debugIcon.breakpointForeground": "#e51400",
		#"debugIcon.breakpointStackframeForeground": "#89d185",
		#"debugIcon.breakpointUnverifiedForeground": "#848484",
		#"debugIcon.continueForeground": "#75beff",
		#"debugIcon.disconnectForeground": "#f48771",
		#"debugIcon.pauseForeground": "#75beff",
		#"debugIcon.restartForeground": "#89d185",
		#"debugIcon.startForeground": "#89d185",
		#"debugIcon.stepBackForeground": "#75beff",
		#"debugIcon.stepIntoForeground": "#75beff",
		#"debugIcon.stepOutForeground": "#75beff",
		#"debugIcon.stepOverForeground": "#75beff",
		#"debugIcon.stopForeground": "#f48771",
		#"debugTokenExpression.boolean": "#75bdfe",
		#"debugTokenExpression.error": "#f48771",
		#"debugTokenExpression.name": BROWN,
		#"debugTokenExpression.number": "#89d185",
		#"debugTokenExpression.string": "#f48771",
		#"debugTokenExpression.value": BROWN,
		#"debugToolBar.background": "#000000",
		#"debugView.exceptionLabelBackground": "#6c2022",
		#"debugView.exceptionLabelForeground": BROWN,
		#"debugView.stateLabelBackground": "#88888844",
		#"debugView.stateLabelForeground": BROWN,
		#"debugView.valueChangedHighlight": "#569cd6",
		#"descriptionForeground": "#d1b897b3",
		#"diffEditor.border": "#b59e7a",
		#"diffEditor.insertedTextBorder": "#33ff2e",
		#"diffEditor.removedTextBorder": "#ff008f",
		#"dropdown.foreground": "#ffffff",
		#"editor.findMatchBorder": "#ffffff00",
		#"editor.findMatchHighlightBorder": "#ffffff00",
		#"editor.findRangeHighlightBorder": "#ffffff00",
		#"editor.focusedStackFrameHighlightBackground": "#7abd7a4d",
		#"editor.hoverHighlightBackground": "#add6ff26",
		#"editor.inactiveSelectionBackground": "#0000ff80",
		#"editor.inlineValuesBackground": "#ffc80033",
		#"editor.inlineValuesForeground": "#ffffff80",
		#"editor.linkedEditingBackground": "#ff00004d",
		#"editor.rangeHighlightBorder": "#ffffff00",
		#"editor.selectionHighlightBorder": "#ffffff00",
		#"editor.snippetFinalTabstopHighlightBorder": "#525252",
		#"editor.snippetTabstopHighlightBackground": "#7c7c7c4d",
		#"editor.stackFrameHighlightBackground": "#ffff0033",
		#"editor.symbolHighlightBorder": "#ffffff00",
		#"editor.wordHighlightBorder": "#ffffff00",
		#"editor.wordHighlightStrongBorder": "#ffffff00",
		#"editorActiveLineNumber.foreground": "#ffffff00",
		#"editorBracketPairGuide.activeBackground1": "#00000000",
		#"editorBracketPairGuide.activeBackground2": "#00000000",
		#"editorBracketPairGuide.activeBackground3": "#00000000",
		#"editorBracketPairGuide.activeBackground4": "#00000000",
		#"editorBracketPairGuide.activeBackground5": "#00000000",
		#"editorBracketPairGuide.activeBackground6": "#00000000",
		#"editorBracketPairGuide.background1": "#00000000",
		#"editorBracketPairGuide.background2": "#00000000",
		#"editorBracketPairGuide.background3": "#00000000",
		#"editorBracketPairGuide.background4": "#00000000",
		#"editorBracketPairGuide.background5": "#00000000",
		#"editorBracketPairGuide.background6": "#00000000",
		#"editorCodeLens.foreground": "#999999",
		#"editorError.border": "#e47777cc",
		#"editorGhostText.border": "#ffffffcc",
		#"editorGroup.focusedEmptyBorder": "#ffffff00",
		#"editorGroupHeader.border": "#b59e7a",
		#"editorGroupHeader.noTabsBackground": DARK_GREEN,
		#"editorGutter.addedBackground": "#33ab4e",
		#"editorGutter.background": DARK_GREEN,
		#"editorGutter.commentRangeForeground": "#c5c5c5",
		#"editorGutter.deletedBackground": "#fc5d6d",
		#"editorGutter.foldingControlForeground": "#ffffff",
		#"editorGutter.modifiedBackground": "#009bf9",
		#"editorHint.border": "#eeeeeecc",
		#"editorHoverWidget.background": "#0c141f",
		#"editorHoverWidget.border": "#b59e7a",
		#"editorHoverWidget.foreground": BROWN,
		#"editorHoverWidget.highlightForeground": "#bdb395",
		#"editorHoverWidget.statusBarBackground": "#0c141f",
		#"editorIndentGuide.activeBackground": "#e3e4e229",
		#"editorIndentGuide.background": "#e3e4e229",
		#"editorInfo.border": "#3794ffcc",
		#"editorInfo.foreground": "#3794ff",
		#"editorInlayHint.background": "#000000",
		#"editorInlayHint.foreground": "#ffffff",
		#"editorInlayHint.parameterBackground": "#000000",
		#"editorInlayHint.parameterForeground": "#ffffff",
		#"editorInlayHint.typeBackground": "#000000",
		#"editorInlayHint.typeForeground": "#ffffff",
		#"editorLightBulb.foreground": "#ffcc00",
		#"editorLightBulbAutoFix.foreground": "#75beff",
		#"editorLink.activeForeground": "#00ffff",
		#"editorMarkerNavigation.background": DARK_GREEN,
		#"editorMarkerNavigationError.background": "#b59e7a",
		#"editorMarkerNavigationInfo.background": "#b59e7a",
		#"editorMarkerNavigationWarning.background": "#b59e7a",
		#"editorMarkerNavigationWarning.headerBackground": "#0c141f",
		#"editorOverviewRuler.addedForeground": "#33ab4e99",
		#"editorOverviewRuler.border": "#7f7f7f4d",
		#"editorOverviewRuler.bracketMatchForeground": "#a0a0a0",
		#"editorOverviewRuler.commonContentForeground": "#c3df6f",
		#"editorOverviewRuler.currentContentForeground": "#c3df6f",
		#"editorOverviewRuler.deletedForeground": "#fc5d6d99",
		#"editorOverviewRuler.errorForeground": "#ff3232",
		#"editorOverviewRuler.findMatchForeground": "#ab5a00",
		#"editorOverviewRuler.incomingContentForeground": "#c3df6f",
		#"editorOverviewRuler.infoForeground": "#3794ffcc",
		#"editorOverviewRuler.modifiedForeground": "#009bf999",
		#"editorOverviewRuler.rangeHighlightForeground": "#007acc99",
		#"editorOverviewRuler.selectionHighlightForeground": "#a0a0a0cc",
		#"editorOverviewRuler.unicodeForeground": "#ab5a00",
		#"editorOverviewRuler.warningForeground": "#ffcc00cc",
		#"editorOverviewRuler.wordHighlightForeground": "#a0a0a0cc",
		#"editorOverviewRuler.wordHighlightStrongForeground": "#c0a0c0cc",
		#"editorPane.background": DARK_GREEN,
		#"editorRuler.foreground": "#ffffff",
		#"editorSuggestWidget.border": "#b59e7a",
		#"editorSuggestWidget.focusHighlightForeground": "#bdb395",
		#"editorSuggestWidgetStatus.foreground": "#cccccc80",
		#"editorUnicodeHighlight.border": "#ff0000",
		#"editorUnnecessaryCode.border": "#ffffffcc",
		#"editorWarning.border": "#ffcc00cc",
		#"editorWhitespace.foreground": "#e3e4e229",
		#"editorWidget.background": "#0c141f",
		#"editorWidget.border": "#b59e7a",
		#"editorWidget.foreground": BROWN,
		#"errorForeground": "#f48771",
		#"extensionBadge.remoteBackground": "#b59e7a",
		#"extensionBadge.remoteForeground": "#000000",
		#"extensionIcon.preReleaseForeground": "#1d9271",
		#"extensionIcon.starForeground": "#ff8e00",
		#"extensionIcon.verifiedForeground": "#3794ff",
		#"gitDecoration.addedResourceForeground": "#1b5225",
		#"gitDecoration.conflictingResourceForeground": "#c74e39",
		#"gitDecoration.deletedResourceForeground": "#c74e39",
		#"gitDecoration.ignoredResourceForeground": "#a7a8a9",
		#"gitDecoration.modifiedResourceForeground": "#e2c08d",
		#"gitDecoration.renamedResourceForeground": "#73c991",
		#"gitDecoration.stageDeletedResourceForeground": "#c74e39",
		#"gitDecoration.stageModifiedResourceForeground": "#e2c08d",
		#"gitDecoration.submoduleResourceForeground": "#8db9e2",
		#"gitDecoration.untrackedResourceForeground": "#73c991",
		#"icon.foreground": "#ffffff",
		#"input.foreground": BROWN,
		#"input.placeholderForeground": "#d1b897b3",
		#"inputOption.activeBackground": "#00000000",
		#"inputOption.activeBorder": "#b59e7a",
		#"inputValidation.errorBackground": "#000000",
		#"inputValidation.errorBorder": "#b59e7a",
		#"inputValidation.infoBackground": "#000000",
		#"inputValidation.infoBorder": "#b59e7a",
		#"inputValidation.warningBackground": "#000000",
		#"inputValidation.warningBorder": "#b59e7a",
		#"interactive.activeCodeBorder": "#b59e7a",
		#"interactive.inactiveCodeBorder": "#b59e7a",
		#"keybindingLabel.background": "#00000000",
		#"keybindingLabel.border": "#6fc3df",
		#"keybindingLabel.bottomBorder": "#6fc3df",
		#"keybindingLabel.foreground": "#ffffff",
		#"list.deemphasizedForeground": "#a7a8a9",
		#"list.filterMatchBorder": "#b59e7a",
		#"list.focusHighlightForeground": "#bdb395",
		#"list.focusOutline": "#ffffff00",
		#"list.invalidItemForeground": "#b89500",
		#"listFilterWidget.background": "#000000",
		#"listFilterWidget.noMatchesOutline": "#b59e7a",
		#"listFilterWidget.outline": "#f38518",
		#"menu.background": "#2a343e",
		#"menu.selectionBorder": "#ffffff00",
		#"menu.separatorBackground": "#b59e7a",
		#"menubar.selectionBorder": "#ffffff00",
		#"menubar.selectionForeground": "#ffffff",
		#"merge.border": "#c3df6f",
		#"minimap.errorHighlight": "#ff3232",
		#"minimap.findMatchHighlight": "#ab5a00",
		#"minimap.foregroundOpacity": "#000000",
		#"minimap.selectionHighlight": "#ffffff",
		#"minimap.selectionOccurrenceHighlight": "#ffffff",
		#"minimap.unicodeHighlight": "#ab5a00",
		#"minimap.warningHighlight": "#ffcc00cc",
		#"minimapGutter.addedBackground": "#33ab4e",
		#"minimapGutter.deletedBackground": "#fc5d6d",
		#"minimapGutter.modifiedBackground": "#009bf9",
		#"minimapSlider.activeBackground": "#b59e7a80",
		#"minimapSlider.background": "#b59e7a52",
		#"minimapSlider.hoverBackground": "#b59e7a80",
		#"notebook.cellBorderColor": "#b59e7a",
		#"notebook.cellInsertionIndicator": "#ffffff00",
		#"notebook.cellStatusBarItemHoverBackground": "#ffffff26",
		#"notebook.cellToolbarSeparator": "#b59e7a",
		#"notebook.focusedCellBorder": "#ffffff00",
		#"notebook.focusedEditorBorder": "#ffffff00",
		#"notebook.inactiveFocusedCellBorder": "#b59e7a",
		#"notebook.inactiveSelectedCellBorder": "#ffffff00",
		#"notebook.selectedCellBorder": "#b59e7a",
		#"notebookScrollbarSlider.activeBackground": "#b59e7a",
		#"notebookScrollbarSlider.background": "#b59e7aa4",
		#"notebookScrollbarSlider.hoverBackground": "#b59e7a",
		#"notebookStatusErrorIcon.foreground": "#f48771",
		#"notebookStatusRunningIcon.foreground": BROWN,
		#"notebookStatusSuccessIcon.foreground": "#89d185",
		#"notificationCenter.border": "#b59e7a",
		#"notificationCenterHeader.background": "#0c141f",
		#"notificationLink.foreground": "#3794ff",
		#"notificationToast.border": "#b59e7a",
		#"notifications.background": "#0c141f",
		#"notifications.border": "#0c141f",
		#"notifications.foreground": BROWN,
		#"notificationsInfoIcon.foreground": "#3794ff",
		#"panel.background": DARK_GREEN,
		#"panel.dropBorder": "#bdb395",
		#"panelSection.border": "#b59e7a",
		#"panelSectionHeader.border": "#b59e7a",
		#"panelTitle.activeBorder": "#b59e7a",
		#"peekViewEditor.matchHighlightBorder": "#ffffff00",
		#"peekViewEditorGutter.background": "#0c141f",
		#"peekViewResult.fileForeground": "#ffffff",
		#"peekViewResult.lineForeground": "#ffffff",
		#"peekViewResult.selectionForeground": "#ffffff",
		#"peekViewTitleDescription.foreground": "#ffffff99",
		#"peekViewTitleLabel.foreground": "#ffffff",
		#"pickerGroup.border": "#ffffff",
		#"pickerGroup.foreground": "#ffffff",
		#"ports.iconRunningProcessForeground": "#b59e7a",
		#"problemsInfoIcon.foreground": "#3794ff",
		#"progressBar.background": "#b59e7a",
		#"quickInput.background": "#0c141f",
		#"quickInput.foreground": BROWN,
		#"quickInputTitle.background": "#000000",
		#"sash.hoverBorder": "#ffffff00",
		#"scm.providerBorder": "#b59e7a",
		#"scrollbarSlider.activeBackground": "#b59e7a",
		#"searchEditor.findMatchBackground": "#63878a8e",
		#"searchEditor.findMatchBorder": "#ffffff00",
		#"searchEditor.textInputBorder": "#b59e7a",
		#"settings.checkboxBackground": "#2a343e",
		#"settings.checkboxBorder": "#b59e7a",
		#"settings.checkboxForeground": "#ffffff",
		#"settings.dropdownBackground": "#2a343e",
		#"settings.dropdownBorder": "#b59e7a",
		#"settings.dropdownForeground": "#ffffff",
		#"settings.dropdownListBorder": "#b59e7a",
		#"settings.focusedRowBorder": "#ffffff00",
		#"settings.headerForeground": "#ffffff",
		#"settings.modifiedItemIndicator": "#00497a",
		#"settings.numberInputBackground": "#2a343e",
		#"settings.numberInputBorder": "#b59e7a",
		#"settings.numberInputForeground": BROWN,
		#"settings.textInputBackground": "#2a343e",
		#"settings.textInputBorder": "#b59e7a",
		#"settings.textInputForeground": BROWN,
		#"sideBar.border": "#b59e7a",
		#"sideBarSectionHeader.border": "#b59e7a",
		#"sideBySideEditor.horizontalBorder": "#b59e7a",
		#"sideBySideEditor.verticalBorder": "#b59e7a",
		#"statusBar.debuggingBackground": "#cc6633",
		#"statusBar.debuggingForeground": "#000000",
		#"statusBar.noFolderBorder": "#b59e7a",
		#"statusBar.noFolderForeground": "#000000",
		#"statusBarItem.activeBackground": "#ffffff2e",
		#"statusBarItem.errorForeground": "#ffffff",
		#"statusBarItem.hoverBackground": "#ffffff1f",
		#"statusBarItem.prominentBackground": "#00000080",
		#"statusBarItem.prominentForeground": "#000000",
		#"statusBarItem.prominentHoverBackground": "#0000004d",
		#"statusBarItem.remoteBackground": "#b59e7a",
		#"statusBarItem.remoteForeground": "#000000",
		#"statusBarItem.warningForeground": "#ffffff",
		#"symbolIcon.arrayForeground": BROWN,
		#"symbolIcon.booleanForeground": BROWN,
		#"symbolIcon.classForeground": "#ee9d28",
		#"symbolIcon.colorForeground": BROWN,
		#"symbolIcon.constantForeground": BROWN,
		#"symbolIcon.constructorForeground": "#b180d7",
		#"symbolIcon.enumeratorForeground": "#ee9d28",
		#"symbolIcon.enumeratorMemberForeground": "#75beff",
		#"symbolIcon.eventForeground": "#ee9d28",
		#"symbolIcon.fieldForeground": "#75beff",
		#"symbolIcon.fileForeground": BROWN,
		#"symbolIcon.folderForeground": BROWN,
		#"symbolIcon.functionForeground": "#b180d7",
		#"symbolIcon.interfaceForeground": "#75beff",
		#"symbolIcon.keyForeground": BROWN,
		#"symbolIcon.keywordForeground": BROWN,
		#"symbolIcon.methodForeground": "#b180d7",
		#"symbolIcon.moduleForeground": BROWN,
		#"symbolIcon.namespaceForeground": BROWN,
		#"symbolIcon.nullForeground": BROWN,
		#"symbolIcon.numberForeground": BROWN,
		#"symbolIcon.objectForeground": BROWN,
		#"symbolIcon.operatorForeground": BROWN,
		#"symbolIcon.packageForeground": BROWN,
		#"symbolIcon.propertyForeground": BROWN,
		#"symbolIcon.referenceForeground": BROWN,
		#"symbolIcon.snippetForeground": BROWN,
		#"symbolIcon.stringForeground": BROWN,
		#"symbolIcon.structForeground": BROWN,
		#"symbolIcon.textForeground": BROWN,
		#"symbolIcon.typeParameterForeground": BROWN,
		#"symbolIcon.unitForeground": BROWN,
		#"symbolIcon.variableForeground": "#75beff",
		#"tab.inactiveModifiedBorder": "#ffffff",
		#"tab.lastPinnedBorder": "#b59e7a",
		#"tab.unfocusedActiveModifiedBorder": "#ffffff",
		#"tab.unfocusedInactiveBackground": "#042327",
		#"tab.unfocusedInactiveForeground": "#ffffff",
		#"tab.unfocusedInactiveModifiedBorder": "#ffffff",
		#"terminal.ansiBlack": "#000000",
		#"terminal.ansiBlue": "#0000ee",
		#"terminal.ansiBrightBlack": "#7f7f7f",
		#"terminal.ansiBrightBlue": "#5c5cff",
		#"terminal.ansiBrightCyan": "#00ffff",
		#"terminal.ansiBrightGreen": "#00ff00",
		#"terminal.ansiBrightMagenta": "#ff00ff",
		#"terminal.ansiBrightRed": "#ff0000",
		#"terminal.ansiBrightWhite": "#ffffff",
		#"terminal.ansiBrightYellow": "#ffff00",
		#"terminal.ansiCyan": "#00cdcd",
		#"terminal.ansiGreen": "#00cd00",
		#"terminal.ansiMagenta": "#cd00cd",
		#"terminal.ansiRed": "#cd0000",
		#"terminal.ansiWhite": "#e5e5e5",
		#"terminal.ansiYellow": "#cdcd00",
		#"terminal.border": "#b59e7a",
		#"terminal.dropBackground": "#63878a1a",
		#"terminal.foreground": "#ffffff",
		#"terminal.selectionBackground": "#ffffff80",
		#"testing.iconErrored": "#f14c4c",
		#"testing.iconFailed": "#f14c4c",
		#"testing.iconPassed": "#73c991",
		#"testing.iconQueued": "#cca700",
		#"testing.iconSkipped": "#848484",
		#"testing.iconUnset": "#848484",
		#"testing.message.error.decorationForeground": "#bdb395",
		#"testing.message.info.decorationForeground": "#bdb39580",
		#"testing.peekBorder": "#b59e7a",
		#"testing.runAction": "#73c991",
		#"textBlockQuote.border": "#ffffff",
		#"textCodeBlock.background": "#000000",
		#"textLink.activeForeground": "#3794ff",
		#"textLink.foreground": "#3794ff",
		#"textPreformat.foreground": "#d7ba7d",
		#"textSeparator.foreground": "#000000",
		#"titleBar.activeForeground": "#ffffff",
		#"toolbar.hoverOutline": "#ffffff00",
		#"tree.indentGuidesStroke": "#a9a9a9",
		#"welcomePage.progress.background": "#2a343e",
		#"welcomePage.progress.foreground": "#3794ff",
		#"welcomePage.tileBackground": "#000000",
		#"window.inactiveBorder": "#b59e7a",
		#"activityBar.activeFocusBorder": null,
		#"banner.foreground": null,
		#"button.secondaryBackground": null,
		#"button.secondaryHoverBackground": null,
		#"charts.red": null,
		#"charts.yellow": null,
		#"diffEditor.diagonalFill": null,
		#"diffEditor.insertedTextBackground": null,
		#"diffEditor.removedTextBackground": null,
		#"editor.findRangeHighlightBackground": null,
		#"editor.foldBackground": null,
		#"editor.snippetFinalTabstopHighlightBackground": null,
		#"editor.snippetTabstopHighlightBorder": null,
		#"editor.symbolHighlightBackground": null,
		#"editor.wordHighlightBackground": null,
		#"editor.wordHighlightStrongBackground": null,
		#"editorError.background": null,
		#"editorError.foreground": null,
		#"editorGhostText.background": null,
		#"editorGhostText.foreground": null,
		#"editorGroup.emptyBackground": null,
		#"editorGroupHeader.tabsBorder": null,
		#"editorHint.foreground": null,
		#"editorInfo.background": null,
		#"editorMarkerNavigationError.headerBackground": null,
		#"editorMarkerNavigationInfo.headerBackground": null,
		#"editorOverviewRuler.background": null,
		#"editorSuggestWidget.selectedForeground": null,
		#"editorSuggestWidget.selectedIconForeground": null,
		#"editorUnnecessaryCode.opacity": null,
		#"editorWarning.background": null,
		#"editorWarning.foreground": null,
		#"editorWidget.resizeBorder": null,
		#"extensionButton.prominentBackground": null,
		#"extensionButton.prominentForeground": null,
		#"extensionButton.prominentHoverBackground": null,
		#"inputOption.activeForeground": null,
		#"inputOption.hoverBackground": null,
		#"inputValidation.errorForeground": null,
		#"inputValidation.infoForeground": null,
		#"inputValidation.warningForeground": null,
		#"keybindingTable.headerBackground": null,
		#"keybindingTable.rowsBackground": null,
		#"list.activeSelectionForeground": null,
		#"list.activeSelectionIconForeground": null,
		#"list.errorForeground": null,
		#"list.filterMatchBackground": null,
		#"list.focusForeground": null,
		#"list.hoverForeground": null,
		#"list.inactiveFocusBackground": null,
		#"list.inactiveFocusOutline": null,
		#"list.inactiveSelectionForeground": null,
		#"list.inactiveSelectionIconForeground": null,
		#"list.warningForeground": null,
		#"menu.selectionForeground": null,
		#"menubar.selectionBackground": null,
		#"merge.commonContentBackground": null,
		#"merge.commonHeaderBackground": null,
		#"merge.currentContentBackground": null,
		#"merge.currentHeaderBackground": null,
		#"merge.incomingContentBackground": null,
		#"merge.incomingHeaderBackground": null,
		#"minimap.background": null,
		#"notebook.cellEditorBackground": null,
		#"notebook.cellHoverBackground": null,
		#"notebook.focusedCellBackground": null,
		#"notebook.outputContainerBackgroundColor": null,
		#"notebook.outputContainerBorderColor": null,
		#"notebook.selectedCellBackground": null,
		#"notebook.symbolHighlightBackground": null,
		#"notificationCenterHeader.foreground": null,
		#"notificationsErrorIcon.foreground": null,
		#"notificationsWarningIcon.foreground": null,
		#"panelInput.border": null,
		#"panelSectionHeader.background": null,
		#"panelSectionHeader.foreground": null,
		#"peekViewResult.matchHighlightBackground": null,
		#"peekViewTitle.background": null,
		#"problemsErrorIcon.foreground": null,
		#"problemsWarningIcon.foreground": null,
		#"quickInputList.focusForeground": null,
		#"quickInputList.focusIconForeground": null,
		#"scrollbar.shadow": null,
		#"selection.background": null,
		#"settings.focusedRowBackground": null,
		#"settings.rowHoverBackground": null,
		#"statusBarItem.errorBackground": null,
		#"statusBarItem.warningBackground": null,
		#"tab.activeBorder": null,
		#"tab.activeBorderTop": null,
		#"tab.activeModifiedBorder": null,
		#"tab.hoverBorder": null,
		#"tab.hoverForeground": null,
		#"tab.unfocusedActiveBorder": null,
		#"tab.unfocusedActiveBorderTop": null,
		#"tab.unfocusedHoverBackground": null,
		#"tab.unfocusedHoverBorder": null,
		#"tab.unfocusedHoverForeground": null,
		#"terminal.background": null,
		#"terminal.tab.activeBorder": null,
		#"terminalCursor.background": null,
		#"terminalCursor.foreground": null,
		#"testing.message.error.lineBackground": null,
		#"testing.message.info.lineBackground": null,
		#"testing.peekHeaderBackground": null,
		#"textBlockQuote.background": null,
		#"titleBar.inactiveForeground": null,
		#"toolbar.activeBackground": null,
		#"toolbar.hoverBackground": null,
		#"tree.tableColumnsBorder": null,
		#"tree.tableOddRowsBackground": null,
		#"walkThrough.embeddedEditorBackground": null,
		#"welcomePage.background": null,
		#"welcomePage.tileHoverBackground": null,
		#"welcomePage.tileShadow": null,
		#"widget.shadow": null
	},
	"tokenColors": [
		{
			"name": "Comment",
			"scope": [
				"comment",
				"punctuation.definition.comment"
			],
			"settings": {
				"fontStyle": "italic",
				"foreground": "#546E7A"
			}
		},
		{
			"name": "Variables",
			"scope": [
				"variable",
				"string constant.other.placeholder"
			],
			"settings": {
				"foreground": "#EEFFFF"
			}
		},
		{
			"name": "Colors",
			"scope": [
				"constant.other.color"
			],
			"settings": {
				"foreground": "#ffffff"
			}
		},
		{
			"name": "Invalid",
			"scope": [
				"invalid",
				"invalid.illegal"
			],
			"settings": {
				"foreground": "#FF5370"
			}
		},
		{
			"name": "Keyword, Storage",
			"scope": [
				"keyword",
				"storage.type",
				"storage.modifier"
			],
			"settings": {
				"foreground": "#C792EA"
			}
		},
		{
			"name": "Operator, Misc",
			"scope": [
				"keyword.control",
				"constant.other.color",
				"punctuation",
				"meta.tag",
				"punctuation.definition.tag",
				"punctuation.separator.inheritance.php",
				"punctuation.definition.tag.html",
				"punctuation.definition.tag.begin.html",
				"punctuation.definition.tag.end.html",
				"punctuation.section.embedded",
				"keyword.other.template",
				"keyword.other.substitution"
			],
			"settings": {
				"foreground": "#89DDFF"
			}
		},
		{
			"name": "Tag",
			"scope": [
				"entity.name.tag",
				"meta.tag.sgml",
				"markup.deleted.git_gutter"
			],
			"settings": {
				"foreground": "#f07178"
			}
		},
		{
			"name": "Function, Special Method",
			"scope": [
				"entity.name.function",
				"meta.function-call",
				"variable.function",
				"support.function",
				"keyword.other.special-method"
			],
			"settings": {
				"foreground": "#82AAFF"
			}
		},
		{
			"name": "Block Level Variables",
			"scope": [
				"meta.block variable.other"
			],
			"settings": {
				"foreground": "#f07178"
			}
		},
		{
			"name": "Other Variable, String Link",
			"scope": [
				"support.other.variable",
				"string.other.link"
			],
			"settings": {
				"foreground": "#f07178"
			}
		},
		{
			"name": "Number, Constant, Function Argument, Tag Attribute, Embedded",
			"scope": [
				"constant.numeric",
				"constant.language",
				"support.constant",
				"constant.character",
				"constant.escape",
				"variable.parameter",
				"keyword.other.unit",
				"keyword.other"
			],
			"settings": {
				"foreground": "#F78C6C"
			}
		},
		{
			"name": "String, Symbols, Inherited Class, Markup Heading",
			"scope": [
				"string",
				"constant.other.symbol",
				"constant.other.key",
				"entity.other.inherited-class",
				"markup.heading",
				"markup.inserted.git_gutter",
				"meta.group.braces.curly constant.other.object.key.js string.unquoted.label.js"
			],
			"settings": {
				"foreground": "#C3E88D"
			}
		},
		{
			"name": "Class, Support",
			"scope": [
				"entity.name",
				"support.type",
				"support.class",
				"support.other.namespace.use.php",
				"meta.use.php",
				"support.other.namespace.php",
				"markup.changed.git_gutter",
				"support.type.sys-types"
			],
			"settings": {
				"foreground": "#FFCB6B"
			}
		},
		{
			"name": "Entity Types",
			"scope": [
				"support.type"
			],
			"settings": {
				"foreground": "#B2CCD6"
			}
		},
		{
			"name": "CSS Class and Support",
			"scope": [
				"source.css support.type.property-name",
				"source.sass support.type.property-name",
				"source.scss support.type.property-name",
				"source.less support.type.property-name",
				"source.stylus support.type.property-name",
				"source.postcss support.type.property-name"
			],
			"settings": {
				"foreground": "#B2CCD6"
			}
		},
		{
			"name": "Sub-methods",
			"scope": [
				"entity.name.module.js",
				"variable.import.parameter.js",
				"variable.other.class.js"
			],
			"settings": {
				"foreground": "#FF5370"
			}
		},
		{
			"name": "Language methods",
			"scope": [
				"variable.language"
			],
			"settings": {
				"fontStyle": "italic",
				"foreground": "#FF5370"
			}
		},
		{
			"name": "entity.name.method.js",
			"scope": [
				"entity.name.method.js"
			],
			"settings": {
				"fontStyle": "italic",
				"foreground": "#82AAFF"
			}
		},
		{
			"name": "meta.method.js",
			"scope": [
				"meta.class-method.js entity.name.function.js",
				"variable.function.constructor"
			],
			"settings": {
				"foreground": "#82AAFF"
			}
		},
		{
			"name": "Attributes",
			"scope": [
				"entity.other.attribute-name"
			],
			"settings": {
				"foreground": "#C792EA"
			}
		},
		{
			"name": "HTML Attributes",
			"scope": [
				"text.html.basic entity.other.attribute-name.html",
				"text.html.basic entity.other.attribute-name"
			],
			"settings": {
				"fontStyle": "italic",
				"foreground": "#FFCB6B"
			}
		},
		{
			"name": "CSS Classes",
			"scope": [
				"entity.other.attribute-name.class"
			],
			"settings": {
				"foreground": "#FFCB6B"
			}
		},
		{
			"name": "CSS ID's",
			"scope": [
				"source.sass keyword.control"
			],
			"settings": {
				"foreground": "#82AAFF"
			}
		},
		{
			"name": "Inserted",
			"scope": [
				"markup.inserted"
			],
			"settings": {
				"foreground": "#C3E88D"
			}
		},
		{
			"name": "Deleted",
			"scope": [
				"markup.deleted"
			],
			"settings": {
				"foreground": "#FF5370"
			}
		},
		{
			"name": "Changed",
			"scope": [
				"markup.changed"
			],
			"settings": {
				"foreground": "#C792EA"
			}
		},
		{
			"name": "Regular Expressions",
			"scope": [
				"string.regexp"
			],
			"settings": {
				"foreground": "#89DDFF"
			}
		},
		{
			"name": "Escape Characters",
			"scope": [
				"constant.character.escape"
			],
			"settings": {
				"foreground": "#89DDFF"
			}
		},
		{
			"name": "URL",
			"scope": [
				"*url*",
				"*link*",
				"*uri*"
			],
			"settings": {
				"fontStyle": "underline"
			}
		},
		{
			"name": "Decorators",
			"scope": [
				"tag.decorator.js entity.name.tag.js",
				"tag.decorator.js punctuation.definition.tag.js"
			],
			"settings": {
				"fontStyle": "italic",
				"foreground": "#82AAFF"
			}
		},
		{
			"name": "ES7 Bind Operator",
			"scope": [
				"source.js constant.other.object.key.js string.unquoted.label.js"
			],
			"settings": {
				"fontStyle": "italic",
				"foreground": "#FF5370"
			}
		},
		{
			"name": "JSON Key - Level 0",
			"scope": [
				"source.json meta.structure.dictionary.json support.type.property-name.json"
			],
			"settings": {
				"foreground": "#C792EA"
			}
		},
		{
			"name": "JSON Key - Level 1",
			"scope": [
				"source.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json support.type.property-name.json"
			],
			"settings": {
				"foreground": "#FFCB6B"
			}
		},
		{
			"name": "JSON Key - Level 2",
			"scope": [
				"source.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json support.type.property-name.json"
			],
			"settings": {
				"foreground": "#F78C6C"
			}
		},
		{
			"name": "JSON Key - Level 3",
			"scope": [
				"source.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json support.type.property-name.json"
			],
			"settings": {
				"foreground": "#FF5370"
			}
		},
		{
			"name": "JSON Key - Level 4",
			"scope": [
				"source.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json support.type.property-name.json"
			],
			"settings": {
				"foreground": "#C17E70"
			}
		},
		{
			"name": "JSON Key - Level 5",
			"scope": [
				"source.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json support.type.property-name.json"
			],
			"settings": {
				"foreground": "#82AAFF"
			}
		},
		{
			"name": "JSON Key - Level 6",
			"scope": [
				"source.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json support.type.property-name.json"
			],
			"settings": {
				"foreground": "#f07178"
			}
		},
		{
			"name": "JSON Key - Level 7",
			"scope": [
				"source.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json support.type.property-name.json"
			],
			"settings": {
				"foreground": "#C792EA"
			}
		},
		{
			"name": "JSON Key - Level 8",
			"scope": [
				"source.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json support.type.property-name.json"
			],
			"settings": {
				"foreground": "#C3E88D"
			}
		},
		{
			"name": "Markdown - Plain",
			"scope": [
				"text.html.markdown",
				"punctuation.definition.list_item.markdown"
			],
			"settings": {
				"foreground": "#EEFFFF"
			}
		},
		{
			"name": "Markdown - Markup Raw Inline",
			"scope": [
				"text.html.markdown markup.inline.raw.markdown"
			],
			"settings": {
				"foreground": "#C792EA"
			}
		},
		{
			"name": "Markdown - Markup Raw Inline Punctuation",
			"scope": [
				"text.html.markdown markup.inline.raw.markdown punctuation.definition.raw.markdown"
			],
			"settings": {
				"foreground": "#65737E"
			}
		},
		{
			"name": "Markdown - Heading",
			"scope": [
				"markdown.heading",
				"markup.heading | markup.heading entity.name",
				"markup.heading.markdown punctuation.definition.heading.markdown"
			],
			"settings": {
				"foreground": "#C3E88D"
			}
		},
		{
			"name": "Markup - Italic",
			"scope": [
				"markup.italic"
			],
			"settings": {
				"fontStyle": "italic",
				"foreground": "#f07178"
			}
		},
		{
			"name": "Markup - Bold",
			"scope": [
				"markup.bold",
				"markup.bold string"
			],
			"settings": {
				"fontStyle": "bold",
				"foreground": "#f07178"
			}
		},
		{
			"name": "Markup - Bold-Italic",
			"scope": [
				"markup.bold markup.italic",
				"markup.italic markup.bold",
				"markup.quote markup.bold",
				"markup.bold markup.italic string",
				"markup.italic markup.bold string",
				"markup.quote markup.bold string"
			],
			"settings": {
				"fontStyle": "bold",
				"foreground": "#f07178"
			}
		},
		{
			"name": "Markup - Underline",
			"scope": [
				"markup.underline"
			],
			"settings": {
				"fontStyle": "underline",
				"foreground": "#F78C6C"
			}
		},
		{
			"name": "Markdown - Blockquote",
			"scope": [
				"markup.quote punctuation.definition.blockquote.markdown"
			],
			"settings": {
				"foreground": "#65737E"
			}
		},
		{
			"name": "Markup - Quote",
			"scope": [
				"markup.quote"
			],
			"settings": {
				"fontStyle": "italic"
			}
		},
		{
			"name": "Markdown - Link",
			"scope": [
				"string.other.link.title.markdown"
			],
			"settings": {
				"foreground": "#82AAFF"
			}
		},
		{
			"name": "Markdown - Link Description",
			"scope": [
				"string.other.link.description.title.markdown"
			],
			"settings": {
				"foreground": "#C792EA"
			}
		},
		{
			"name": "Markdown - Link Anchor",
			"scope": [
				"constant.other.reference.link.markdown"
			],
			"settings": {
				"foreground": "#FFCB6B"
			}
		},
		{
			"name": "Markup - Raw Block",
			"scope": [
				"markup.raw.block"
			],
			"settings": {
				"foreground": "#C792EA"
			}
		},
		{
			"name": "Markdown - Raw Block Fenced",
			"scope": [
				"markup.raw.block.fenced.markdown"
			],
			"settings": {
				"foreground": "#00000050"
			}
		},
		{
			"name": "Markdown - Fenced Bode Block",
			"scope": [
				"punctuation.definition.fenced.markdown"
			],
			"settings": {
				"foreground": "#00000050"
			}
		},
		{
			"name": "Markdown - Fenced Bode Block Variable",
			"scope": [
				"markup.raw.block.fenced.markdown",
				"variable.language.fenced.markdown",
				"punctuation.section.class.end"
			],
			"settings": {
				"foreground": "#EEFFFF"
			}
		},
		{
			"name": "Markdown - Fenced Language",
			"scope": [
				"variable.language.fenced.markdown"
			],
			"settings": {
				"foreground": "#65737E"
			}
		},
		{
			"name": "Markdown - Separator",
			"scope": [
				"meta.separator"
			],
			"settings": {
				"fontStyle": "bold",
				"foreground": "#65737E"
			}
		},
		{
			"name": "Markup - Table",
			"scope": [
				"markup.table"
			],
			"settings": {
				"foreground": "#EEFFFF"
			}
		},
	]
}


print(json.dumps(theme, indent=2, sort_keys=True))
