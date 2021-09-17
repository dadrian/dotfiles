" Vim color file
" Maintainer:	David Adrian <davidcadrian@gmail.com>

" This color scheme is based on the one used by Jonathan Blow
"
"

" First remove all existing highlighting.
set background=dark
hi clear
if exists("syntax_on")
  syntax reset
endif

" David edits
hi Normal ctermfg=Brown ctermbg=DarkBlue guifg=#d1b897 guibg=#062626
hi NonText term=bold cterm=bold ctermfg=LightBlue ctermbg=DarkBlue gui=bold guifg=LightBlue guibg=#062626

hi Comment guifg=#44b340 ctermfg=Green

hi Constant term=None cterm=None ctermfg=LightGray gui=None guifg=#7ad0c6
hi String ctermfg=LightBlue guifg=#2ec09c
hi Character ctermfg=LightBlue guifg=#2ec09c
hi Number ctermfg=DarkBlue guifg=#7ad0c6
hi Float ctermfg=DarkBlue guifg=#7ad0c6
hi Boolean ctermfg=DarkBlue guifg=#b0a0f0

hi Identifier guifg=#c1d1e3
hi Function guifg=#FFFFFF

hi Statement term=bold cterm=bold gui=none guifg=#ffffff

hi Special term=bold gui=bold ctermfg=DarkMagenta guifg=#C07010

hi Type gui=None guifg=#8cde94

hi PreProc gui=None term=None cterm=None ctermfg=LightGray guifg=#8cde94

hi Ignore ctermfg=White guifg=White

" Cursor
" This doesn't seem to work reliably
hi Cursor guibg=#8cde94
hi link iCursor Cursor
hi link rCursor Cursor
hi CursorLine guifg=inverse guibg=inverse
hi link CursorColumn CursorLine

hi Visual term=reverse ctermbg=Blue guibg=#0000ff guifg=None
hi Search term=reverse ctermbg=LightMagenta ctermfg=None guibg=#F9D9D9 guifg=#062626
hi link IncSearch Search
hi MatchParen term=standout cterm=standout guibg=#0b3335

hi Error term=standout ctermfg=White ctermbg=Red gui=underline guibg=None guifg=#ff0000
hi Todo term=standout ctermfg=Blue ctermbg=Yellow gui=none guibg=None guifg=#ffaa00
hi Directory term=bold ctermfg=DarkBlue guifg=#7ad0c6

" Color of the tabs
hi TabLine cterm=none ctermfg=DarkBlue ctermbg=Brown gui=none guifg=#062626 guibg=#d1b897
hi TabLineSel term=bold cterm=bold ctermfg=Brown ctermbg=DarkBlue gui=bold guibg=#062626 guifg=#d1b897
hi TabLineFill ctermbg=Brown guibg=#d1b897

" Insert / normal / etc mode message at the bottom line
hi ModeMsg term=bold cterm=bold gui=bold

" I haven't gone through this section yet
hi StatusLine term=reverse,bold cterm=reverse,bold gui=reverse,bold
hi StatusLineNC term=reverse cterm=reverse gui=reverse
hi VertSplit term=reverse cterm=reverse gui=reverse
hi DiffText term=reverse cterm=bold ctermbg=Red gui=bold guibg=Red
hi LineNr term=underline ctermfg=Brown guifg=Brown
hi MoreMsg term=bold ctermfg=DarkGreen gui=bold guifg=SeaGreen
hi Question term=standout ctermfg=DarkGreen gui=bold guifg=SeaGreen
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
