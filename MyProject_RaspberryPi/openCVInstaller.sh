installer(){
    printf '*%.0s' {1..10}
    echo "\n"
    if [ $1 -eq 0 ]
    then
        echo "good to go!"
    else
        echo "Problem with the last command!!"
        exit 1
    fi
}

ls
installer $?
