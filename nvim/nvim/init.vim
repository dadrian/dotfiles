" Neovim configuration

" Configure and install Vim Plug
let data_dir = stdpath('data') . '/site'
if empty(glob(data_dir . '/autoload/plug.vim'))
  " Vim Plug wants to be in the data directory
  if has('unix') || has('win32unix') || has('win64unix')
    silent execute '!mkdir -p '.data_dir.'/autoload'
    silent execute '!cp '.stdpath('config').'/_cache/plug.vim '.data_dir.'/autoload/plug.vim'
  else
    "something with robocopy
    "silent execute '!robocopy'.stdpath('config').'\_cache\plug.vim '.data_dir.'\autoload\plug.vim'
  endif
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

" Use the plugins
call plug#begin(stdpath('config') . '/plugged')
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries', 'tag': 'v1.24' }
call plug#end()

" Nice colors in the terminal
set termguicolors

" This is probably default, but playing it safe
syntax enable

" Set highlight group, block/vertifical, and blinking for the cursor
set guicursor=n-v-c:block-Cursor
set guicursor+=i-ci-ve:blinkwait10-blinkon100-ver25-iCursor
set guicursor+=r-cr-o:hor20-rCursor
set guicursor+=n-v-c:blinkon0

" Terminal detection happens after config load, so wait until that's all done
" to set the color scheme (which requires 24-bit color to look good)
autocmd VimEnter * colorscheme dadrian

" Install missing plugins
autocmd VimEnter * if len(filter(values(g:plugs), '!isdirectory(v:val.dir)'))
  \| PlugInstall --sync | source $MYVIMRC
\| endif


