# Revision History for pyniggli

## Revision 0.1.6
- Added an option to print the steps taken to reduce the cell.
- Updated the floating point tolerance to better reflect the original
  paper.
- Changed the algorithm so that it now calculates the niggli G vector
  from the updated (partially reduced) lattice after each step to
  improve stability.
- Changed steps 3 and 4 to work of integer values rather than the
  actual floats to improve stability.
- Re-organized some of the condition checks to improve stability.
- Added a printing of the original lattice vectors to the debug
  raises.
- Changed _find_C3 and _find_C4 to static methods that take integers
  rather than floats.

## Revision 0.1.5
- Fixed issue reported in [issue #5](https://github.com/wsmorgan/pyniggli/issues/5).
- Updated the floating point tolerance to depend on cell volume.
- Increased the number of allowed iterations to allow for larger cells.

## Revision 0.1.4
- Improved the tolerance on floating point comparisons in the Niggli
  condition checker.

## 0.1.3
- Added Niggli condition checks to the subroutine. The class now
  issues a RuntimeError if the Niggli conditions aren't met.
- Changed some of the comparisons to be np.allclose.

## 0.1.2
-Fixed the niggli reduction so that the values of the angles are used
 to contsruct the transformation matrix before they are reassigned.
-Fixed condition 7 which was changing the value of C instead of B.

## 0.1.2
-Fixed niggli so that the columns and not the rows are used to colculate the constants.
-Shortened the calls in the inequalities slightly.

## 0.1.1
-Fixed the call to swap in niggli.py.

## 0.1.0
-Created main niggli class and the subroutines needed to perform the
 niggli reduction.

## 0.0.1
-Created repo.