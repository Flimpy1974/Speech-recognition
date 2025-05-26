#!/bin/sh
#dotnet tool install --global Microsoft.CognitiveServices.Speech.CLI

clear
# Configure the Speech CLI with your Azure subscription key and region#spx config @key --set 13193735-a05b-411c-8a26-e01c94aa6a33
#spx config @key --set aec53e8eb1a644f88c8ddc1647147975  > /dev/null
#spx config @region --set swedencentral > /dev/null

#spx config @key > /dev/null
#spx config @region > /dev/null

#rm parlout_*.mp3
#rm parl1.mp4.rtf
rm ./result/*.*
rm ./processing/*.*

# Download the audio file from Azure Storage
#echo "Downloading the mp4 file...."
#az storage blob downltesoad --account-name mystortaras --container-name parliament --name parl1.mp4 --file parl1.mp4 --auth-mode login


echo "Extracting audio data from video...."

for inputfile in "."/input_video/*.mp4; do

  echo "$inputfile"
  shortfilename=$(basename "$inputfile")
  shortfilename="${shortfilename%.*}"
  echo "blala $shortfilename"

  ./ffmpeg/bin/ffmpeg -i $inputfile  -vn -f segment -segment_time 2400 -ar 22050 -ac 1 -b:a 16k "./processing/parlout_$shortfilename-%03d.mp3" -y
  #./ffmpeg/bin/ffmpeg -i parl1_big.mp4 -ss 2100  -t 1800 -vn -f segment -segment_time 650 -ar 22050 -ac 1 -b:a 16k ./processing/parlout_$shortfilename%03d.mp3 -y

  #echo "Recognizing text...."
  #spx recognize --file parl1.mp4.wav --output file parl1.mp4.rtf --language de-DE > NUL 2>&1


  if [ -f "./result/$shortfilename.rtf" ]; then
    rm "./result/$shortfilename.rtf"
    echo "./result/$shortfilename.rtft_loop.sh File deleted."
  fi


  for file in "."/processing/parlout_$shortfilename*.mp3; do
  echo "Processing $file"
  curl https://xxxxxxxxxxxx.openai.azure.com/openai/deployments/whisper/audio/transcriptions?api-version=2024-02-01 \
  -H "api-key: fxxxxxxxxxxxxxxxxxxx" \
  -H "Content-Type: multipart/form-data" \
  -F file="@$file" \
  >> ./result/$shortfilename.rtf
  #-o parl1.mp4.rtf
  done
done


echo "Summarizing text...."
#python summarize_gpt4.py
 




