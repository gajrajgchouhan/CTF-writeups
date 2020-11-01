# unzip nested encrypted zip files with password as their name
while true
do
    find . -type f -name "*.zip" -execdir sh -c 'echo "doing {}"; unzip -q -P $(basename {} ".zip") {};' \; -delete
done