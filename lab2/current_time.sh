#!/bin/bash
current_hour=$(date +%H)
current_min=$(date +%M)
end_hour=18
end_min=0

current_total=$((current_hour * 60 + current_min))
end_total=$((end_hour * 60 + end_min))
remaining=$((end_total - current_total))

if [ $remaining -ge 0 ]; then
  hours=$((remaining / 60))
  mins=$((remaining % 60))
  echo "Current time: ${current_hour}${current_min}"
  echo "Work day ends after ${hours} hours and ${mins} minutes."
else
  echo "Work day has ended."
fi
