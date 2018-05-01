" .vimrc
" Configuration file for vim

colorscheme darkblue 	" Anything but the default
set number		" Line numbers

set expandtab           " Insert spaces when tabbing

" Tab settings for specific file types
autocmd Filetype python setlocal tabstop=4 shiftwidth=4 softtabstop=4
autocmd Filetype c setlocal tabstop=2 shiftwidth=2 softtabstop=2
autocmd Filetype spec setlocal tabstop=4 shiftwidth=4 softtabstop=4
autocmd Filetype xml setlocal tabstop=2 shiftwidth=2 softtabstop=2

" Coloring settings for vimdiff
highlight Normal term=none cterm=none ctermfg=White ctermbg=Black gui=none guifg=White guibg=Black
highlight DiffAdd cterm=none ctermfg=fg ctermbg=Blue gui=none guifg=fg guibg=Blue
highlight DiffDelete cterm=none ctermfg=fg ctermbg=Blue gui=none guifg=fg guibg=Blue
highlight DiffChange cterm=none ctermfg=fg ctermbg=Blue gui=none guifg=fg guibg=Blue
highlight DiffText cterm=none ctermfg=bg ctermbg=White gui=none guifg=bg guibg=White
