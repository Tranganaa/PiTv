#! /bin/bash
git add .
while getopts ":m:" opt; do
  case $opt in
    m)
      git commit -m "$OPTARG">&2
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

