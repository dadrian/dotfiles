" Vim color file
" Maintainer:	David Adrian <davidcadrian@gmail.com>

" This color scheme is based on the one used by Jonathan Blow
"
"

" First remove all existing highlighting.
set background=light
hi clear
if exists("syntax_on")
  syntax reset
endif

" David edits
hi Normal ctermfg=Brown ctermbg=DarkBlue guifg=#80845E guibg=#042328
hi NonText term=bold cterm=bold ctermfg=LightBlue ctermbg=DarkBlue gui=bold guifg=LightBlue guibg=#042328

hi Comment guifg=Green ctermfg=Green

hi Constant term=None cterm=None ctermfg=LightGray gui=None guifg=#80A0A0
hi String ctermfg=LightBlue guifg=#40B0B0
hi Character ctermfg=LightBlue guifg=#40B0B0
hi Number ctermfg=DarkBlue guifg=#B0A0E0
hi Float ctermfg=DarkBlue guifg=#B0A0E0
hi Boolean ctermfg=DarkBlue guifg=#B0A0E0

hi Identifier guifg=#80A0A0
hi Function guifg=#80A0A0

hi Statement term=bold cterm=bold gui=bold guifg=#B0C0D0

hi Special term=bold gui=bold ctermfg=DarkMagenta guifg=#C07010

hi Type gui=None guifg=#80D090

hi PreProc gui=None term=None cterm=None ctermfg=LightGray guifg=#B0C0D0

hi Ignore ctermfg=White guifg=White

" Cursor
" This doesn't seem to work reliably
hi Cursor gui=none guifg=inverse guibg=blue
hi lCursor guibg=Black guifg=NONE
hi CursorLine gui=none guifg=inverse guibg=inverse
hi link CursorColumn CursorLine

" Groups used in the 'highlight' and 'guicursor' options default value.
"
" I haven't gone through this section yet
hi ErrorMsg term=standout ctermbg=DarkRed ctermfg=White guibg=Red guifg=White
hi IncSearch term=reverse cterm=reverse gui=reverse
hi ModeMsg term=bold cterm=bold gui=bold
hi StatusLine term=reverse,bold cterm=reverse,bold gui=reverse,bold
hi StatusLineNC term=reverse cterm=reverse gui=reverse
hi VertSplit term=reverse cterm=reverse gui=reverse
hi Visual term=reverse ctermbg=grey guibg=grey80
hi DiffText term=reverse cterm=bold ctermbg=Red gui=bold guibg=Red
hi Directory term=bold ctermfg=DarkBlue guifg=Blue
hi LineNr term=underline ctermfg=Brown guifg=Brown
hi MoreMsg term=bold ctermfg=DarkGreen gui=bold guifg=SeaGreen
hi Question term=standout ctermfg=DarkGreen gui=bold guifg=SeaGreen
hi Search term=reverse ctermbg=Yellow ctermfg=NONE guibg=Yellow guifg=NONE
hi SpecialKey term=bold ctermfg=DarkBlue guifg=Blue
hi Title term=bold ctermfg=DarkMagenta gui=bold guifg=Magenta
hi WarningMsg term=standout ctermfg=DarkRed guifg=Red
hi WildMenu term=standout ctermbg=Yellow ctermfg=Black guibg=Yellow guifg=Black
hi Folded term=standout ctermbg=Grey ctermfg=DarkBlue guibg=LightGrey guifg=DarkBlue
hi FoldColumn term=standout ctermbg=Grey ctermfg=DarkBlue guibg=Grey guifg=DarkBlue
hi DiffAdd term=bold ctermbg=LightBlue guibg=LightBlue
hi DiffChange term=bold ctermbg=LightMagenta guibg=#B0A0E0
hi DiffDelete term=bold ctermfg=Blue ctermbg=LightCyan gui=bold guifg=Blue guibg=LightCyan

" vim: sw=2
