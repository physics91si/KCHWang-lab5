## Feedback

* Good!
* A couple of minor stylistic points:
  * In `trig.py`, it would be nicer to define the `integrate` function to be able to take in a single number for `dx`.
  * For list slicing (`list[start:end]`), if you leave out one of the slicing indices, it will default to the start or end of the list as appropriate, so for example, you could write
`low_pass_filter[num_freq//25:] = 0`
and leave out the `num_freq` at the end (similarly, if the slice starts at the beginning of the list, you can leave out the first index).
