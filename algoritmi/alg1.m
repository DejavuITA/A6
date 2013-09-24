function retval = mmhg_to_pa (v)
  retval = 0;
  if (is_vector (v))
    retval = v .* 133.322;
  else
    retval = v * 133.322;
  endif
endfunction

function retval = pa_to_mmhg (v)
  retval = 0;
  if (is_vector (v))
    retval = v ./ 133.322;
  else
    retval = v / 133.322;
  endif
endfunction

function retval = atm_to_pa (v)
  retval = 0;
  if (is_vector (v))
    retval = v .* 101325;
  else
    retval = v * 101325;
  endif
endfunction

function retval = pa_to_atm (v)
  retval = 0;
  if (is_vector (v))
    retval = v ./ 101325;
  else
    retval = v / 101325;
  endif
endfunction