" Vim color file
" Maintainer:	David Adrian <davidcadrian@gmail.com>

" This color scheme is stolen from Jonathan Blow
"
"

" First remove all existing highlighting.
set background=light
hi clear
if exists("syntax_on")
  syntax reset
endif

" David edits
" Green=#008000
hi Normal ctermfg=Black ctermbg=Black guifg=#80845E guibg=#042328
hi Comment guifg=Green ctermfg=Green

hi Constant term=bold gui=standout ctermfg=DarkRed guifg=Magenta
hi Special term=bold gui=bold ctermfg=DarkMagenta guifg=Red guibg=grey95
hi Statement term=bold cterm=bold ctermfg=Brown gui=bold guifg=#A7C1C7
hi Identifier guifg=Red
hi Ignore ctermfg=LightGrey guifg=grey90



" Groups used in the 'highlight' and 'guicursor' options default value.
hi ErrorMsg term=standout ctermbg=DarkRed ctermfg=White guibg=Red guifg=White
hi IncSearch term=reverse cterm=reverse gui=reverse
hi ModeMsg term=bold cterm=bold gui=bold
hi StatusLine term=reverse,bold cterm=reverse,bold gui=reverse,bold
hi StatusLineNC term=reverse cterm=reverse gui=reverse
hi VertSplit term=reverse cterm=reverse gui=reverse
hi Visual term=reverse ctermbg=grey guibg=grey80
hi DiffText term=reverse cterm=bold ctermbg=Red gui=bold guibg=Red
hi Cursor guibg=Green guifg=NONE
hi lCursor guibg=Cyan guifg=NONE
hi Directory term=bold ctermfg=DarkBlue guifg=Blue
hi LineNr term=underline ctermfg=Brown guifg=Brown
hi MoreMsg term=bold ctermfg=DarkGreen gui=bold guifg=SeaGreen
hi NonText term=bold ctermfg=Blue gui=bold guifg=Blue guibg=grey80
hi Question term=standout ctermfg=DarkGreen gui=bold guifg=SeaGreen
hi Search term=reverse ctermbg=Yellow ctermfg=NONE guibg=Yellow guifg=NONE
hi SpecialKey term=bold ctermfg=DarkBlue guifg=Blue
hi Title term=bold ctermfg=DarkMagenta gui=bold guifg=Magenta
hi WarningMsg term=standout ctermfg=DarkRed guifg=Red
hi WildMenu term=standout ctermbg=Yellow ctermfg=Black guibg=Yellow guifg=Black
hi Folded term=standout ctermbg=Grey ctermfg=DarkBlue guibg=LightGrey guifg=DarkBlue
hi FoldColumn term=standout ctermbg=Grey ctermfg=DarkBlue guibg=Grey guifg=DarkBlue
hi DiffAdd term=bold ctermbg=LightBlue guibg=LightBlue
hi DiffChange term=bold ctermbg=LightMagenta guibg=LightMagenta
hi DiffDelete term=bold ctermfg=Blue ctermbg=LightCyan gui=bold guifg=Blue guibg=LightCyan
hi CursorLine term=underline cterm=underline guibg=grey80
hi CursorColumn term=reverse ctermbg=grey guibg=grey80

" Colors for syntax highlighting
"
" vim: sw=2
