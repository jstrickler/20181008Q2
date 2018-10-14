for x in *.py
do 
    echo "*** $x ***"
    if [ -f "~/py/examples3/$x" ]
    then 
        diff $x ~/py/examples3
    fi
done
