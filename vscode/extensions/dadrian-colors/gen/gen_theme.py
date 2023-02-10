#!/usr/bin/env python3
import json
from logging.config import IDENTIFIER

INVISIBLE = '#ffffff00' # white with no opacity
NONE = '#00000000'

BROWN = '#d1b897'
LIGHT_BROWN = '#bdb395'
DARK_BROWN = '#80845e'
DARK_GREEN = '#062626'
TURQUOISE = '#40b0b0'

LIGHT_GRAY = '#63878a'
DARK_GRAY = '#2a343e'
LIGHT_BLUE= '#7ad0c6'
BRIGHT_BLUE = '#40b0b0'

DARK_BLUE = '#0c141f'

STRING = BRIGHT_BLUE
CHAR = BRIGHT_BLUE
NUMBER = LIGHT_BLUE
FLOAT = LIGHT_BLUE

ORANGE = '#c07010'


RED = '#e83020'
GREEN = '#30C030'
LIGHT_GREEN = '#8cde94'
BLACK = '#000000'

BLUE = '#0000ff'
BLUE_HIGHLIGHT = BLUE + '8e'

VISUAL = BLUE
VISUAL_HIGHLIGHT = BLUE_HIGHLIGHT

PINK = '#f9d9d9'
SEARCH = PINK

BACKGROUND = DARK_GREEN
DARK_BACKGROUND = DARK_BLUE

FOREGROUND = BROWN
TEXT = BROWN
TRANSPARENT_TEXT = TEXT + '00'
STRINGS = TURQUOISE

GRAY = '#63878a'
HIGHLIGHT_GRAY = '#63878a8e'
HIGHLIGHT_GRAY_LESS = '#63878a1a'

DARK_GRAY = '#2a343e'
BLUE_GRAY = '#0b3335'

OFF_WHITE = '#c1d1e3'
WHITE = '#FFFFFF'

COMMENT = GREEN
CONSTANT = LIGHT_BLUE
NUMBER = BRIGHT_BLUE
ERROR = RED
WEAK_ERROR = '#f48771'
WARNING = ORANGE

IDENTIFIER = OFF_WHITE
FUNCTION = WHITE
TYPE = LIGHT_GREEN
STATEMENT = WHITE
KEYWORD = STATEMENT

CURSOR = LIGHT_GREEN



theme = {
	"name": "dadrian",
	"type": "hc",
	"colors": {
		"errorForeground": ERROR,
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
        "editor.foldBackground": FOREGROUND + '65',
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
		"editorError.foreground": ERROR,
		"editorGroup.border": FOREGROUND,
		"editorGroup.dropBackground": HIGHLIGHT_GRAY_LESS,
        "editorGroupHeader.border": FOREGROUND,
        "editorGroupHeader.tabsBorder": FOREGROUND + '53',
		"editorGroupHeader.tabsBackground": BACKGROUND,
		"editorGroupHeader.noTabsBackground": BACKGROUND,
		"editorGroupHeader.noTabsBorder": FOREGROUND,
        "tab.activeBackground": FOREGROUND + '53',
        "tab.activeForeground": WHITE,
        "tab.border": FOREGROUND + '53',
		"tab.activeBorder": FOREGROUND,
		"tab.activeBorderTop": FOREGROUND,
        "tab.hoverBackground": FOREGROUND + '53',
        "tab.inactiveBackground": BACKGROUND,
        "tab.inactiveForeground": OFF_WHITE,
        "tab.unfocusedActiveBackground": FOREGROUND + '32',
        "tab.unfocusedActiveForeground": WHITE,
		"editorLineNumber.activeForeground": FOREGROUND,
		"editorLineNumber.foreground": FOREGROUND + '65',
		"editorSuggestWidget.background": BACKGROUND,
		"editorSuggestWidget.foreground": OFF_WHITE,
		"editorSuggestWidget.highlightForeground": FOREGROUND,
		"editorSuggestWidget.selectedBackground": FOREGROUND + '65',
		"focusBorder": WHITE + '00',
		"foreground": OFF_WHITE,
		"input.background": DARK_GRAY, # Literal text box for inputs, e.g. Cmd-F
		"input.border": FOREGROUND,
		"list.errorForeground": ERROR,
		"list.warningForeground": ORANGE,
		"list.activeSelectionBackground": FOREGROUND,
        "list.activeSelectionForeground": BACKGROUND,
		"list.dropBackground": "#63878a1a",
		"list.focusBackground": FOREGROUND + 'a4',
		"list.highlightForeground": LIGHT_BROWN,
		"list.hoverBackground": FOREGROUND + '65',
		"list.inactiveSelectionBackground": FOREGROUND + 'a4',
        "list.inactiveSelectionForeground": OFF_WHITE,
		"menu.border": FOREGROUND,
		"menu.foreground": OFF_WHITE,
		"menu.selectionBackground": FOREGROUND + '65',
		"panel.border": FOREGROUND,
		"panelSectionHeader.foreground": WHITE,
		"panelSection.dropBackground": BACKGROUND + '1a',
		"panelTitle.activeForeground": LIGHT_BROWN,
		"panelTitle.inactiveForeground": OFF_WHITE,
		"peekView.border": FOREGROUND,
		"peekViewEditor.background": DARK_BACKGROUND,
		"peekViewEditor.matchHighlightBackground": GRAY + '8e',
		"peekViewResult.background": DARK_BACKGROUND,
		"peekViewResult.selectionBackground": FOREGROUND,
		"quickInputList.focusBackground": FOREGROUND + 'a4',
		"scrollbarSlider.background": "#b59e7aa4",
		"scrollbarSlider.hoverBackground": "#b59e7a",
		"sideBar.background": BACKGROUND,
		"sideBar.foreground": OFF_WHITE,
		"statusBar.border": FOREGROUND,
		"sideBar.dropBackground": BACKGROUND + '1a',
		"sideBarSectionHeader.background": "#b59e7a",
		"sideBarSectionHeader.foreground": "#000000",
		"sideBarTitle.foreground": "#bbbbbb",
		"statusBar.background": "#b59e7a",
		"statusBar.debuggingBorder": "#b59e7a",
		"statusBar.foreground": "#000000",
		"statusBar.noFolderBackground": "#b59e7a",
		"titleBar.activeBackground": BACKGROUND,
		"titleBar.border": FOREGROUND,
		"titleBar.inactiveBackground": DARK_BACKGROUND,
		"window.activeBorder": FOREGROUND,
	},
	"tokenColors": [
		{
			"name": "Comment",
			"scope": [
				"comment",
                "punctuation.definition.comment",
			],
			"settings": {
				"foreground": COMMENT,
			}
		},
		{
			"name": "Variables",
			"scope": [
				"variable",
			],
			"settings": {
				"foreground": TEXT,
			}
		},
		{
			"name": "Storage",
			"scope": [
				"storage.type",
				"storage.modifier"
			],
			"settings": {
				"foreground": TYPE,
			}
		},
		{
			"name": "Keyword",
			"scope": [
				"keyword",
			],
			"settings": {
				"foreground": KEYWORD,
			}
		},
		{
			"name": "Invalid",
			"scope": [
				"invalid",
			],
			"settings": {
				"foreground": ERROR,
			}
		},
		{
			"name": "Strings",
			"scope": [
				"string",
                "punctuation.definition.string",
			],
			"settings": {
				"foreground": STRING,
			}
		},
		{
			"name": "Punctuation",
			"scope": [
				"punctuation",
			],
			"settings": {
				"foreground": TEXT,
			}
		},
		{
			"name": "Special",
			"scope": [
                "constant.character.escape"
			],
			"settings": {
				"foreground": ORANGE,
                "fontStyle": "bold",
			}
		},
		{
			"name": "Overrides to Text",
			"scope": [
				"keyword.other.unit",
			],
			"settings": {
				"foreground": TEXT,
			}
		},

	]
}


print(json.dumps(theme, indent=2, sort_keys=True))
