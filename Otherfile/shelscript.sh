gitdiffvariable=$(git diff --staged)
$gitdiffvariable
if [ -z "$gitdiffvariable" ]
then
      echo "\$gitdiffvariable is empty"
else
      echo "\$gitdiffvariable is NOT empty"
fi