#!/bin/bash

#Check that script is run from root directory
if [[ ! ( "$0" =~ (\./)?scripts/createYear.sh ) ]]; then
	echo "Please run this script from the base directory as \"scripts/createYear.sh\"."
	exit 1
fi

# Check that correct amount of arguments are supplied
if [[ $# -ne 1 ]]; then
	echo -e "\033[31mInvalid arguments supplied!\033[39m\nPlease make sure to run this command as 'scripts/createYear.sh <Year to create>'."
	exit 1
# Check that a number is supplied
elif [[ ! ($1 =~ ^[0-9]+$) ]]; then
	echo -e "\033[31mInvalid argument supplied!\033[39m\nPlease make sure to pass a year as argument like 'scripts/createYear.sh <Year to create>'."
	exit 1
elif [[ $1 -lt 2015 ]]; then
	echo -e "\033[96mSkipping:\033[39m No Advent of Code before 2015."
	exit 0
fi

year=$1
addDays=""

# Check that years haven't already been created
if [[ -d "input/$year" && -d "src/$year" && -d "iclude/$year" ]]; then
	echo -e "\033[96mSkipping:\033[39m Year already exists."
	exit 0
fi

mkdir -p "input/$year" "years/_$year"

# Copy day templates
for day in {1..25}; do
	addDays+="\tyears.set_day($year, $day, _$year.day$day.Day${day}_$year())\n"

	if [[ -f "years/_$year/day$day.py" ]]; then
		continue
	fi

	cp "template/day.py" "years/_$year/day$day.py"

	# Adjust to fit day
	sed -i "s/\(\<Day\>\)/\1$day\_$year/g; s/AoCDay(0, 0)/AoCDay($year, $day)/g" "years/_$year/day$day.py"
done

# Add module
cp "template/__init__.py" "years/_$year/__init__.py"

# Update years module to include new year
grep -qxF "_2015" years/__init__.py || sed -i "s/\[\(\"_[0-9]\{4\}\", \)*\]/[\1\"_$year\", ]/g" "years/__init__.py"

# Add days to main.py
# Add days in main.cpp
mainFile=""
addFunctionCall="false"

while IFS= read -r line; do
	# Check for start of "year" section
    if [[ "$line" == *"def set_years(years: AoCYears):"* ]]; then
    	addFunctionCall="true"
	fi

	# Add call
	if [[ "$addFunctionCall" == "true" ]]; then
		if [[ "$line" == *"set_days_$year(years)"* ]]; then
    		addFunctionCall="false"
    	elif [[ "$line" == *"pass"* ]]; then
    		addFunctionCall="false"
    		mainFile+="\tset_days_$year(years)\n"
    		continue
    	elif [[ "$line" == "\n" ]]; then
    		addFunctionCall="false"
    		mainFile+="\tset_days_$year(years)\n"
    	fi
	fi

    mainFile+="$line\n"
done < main.py

if [[ ! ("$mainFile" == *"void setDays$year(AoCYears *years)\n"*) ]]; then
	mainFile+="\n\ndef set_days_$year(years: AoCYears):\n$addDays"
fi

echo -e "$mainFile" > main.py
sed -i 's/    /\t/g' main.py
