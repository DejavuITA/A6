function retval = mmhg_to_pa (v)
  retval = 0;
  retval = v .* 133.322;
endfunction

function retval = pa_to_mmhg (v)
  retval = 0;
  retval = v ./ 133.322;
endfunction

function retval = atm_to_pa (v)
  retval = 0;
  retval = v .* 101325;
endfunction

function retval = pa_to_atm (v)
  retval = 0;
  retval = v ./ 101325;
endfunction