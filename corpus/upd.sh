#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "usage: $0 <vocab_file>"
    exit
fi

if [[ -e $1 ]]; then
    echo ">> Generating vocabulary file..."
    for word in `cat $1 | cut -d '#' -f 1 | tr -d " "`
        do echo $word >> vocab
    done

    URL="http://www.speech.cs.cmu.edu"

    echo ">> Uploading vocabulary corpus..."
    RESPONSE=`curl -sL -H "Content-Type: multipart/form-data" -F "corpus=@vocab" -F "formtype=simple" $URL/cgi-bin/tools/lmtool/run/`
    rm vocab

    REF_URL=`echo $RESPONSE | grep -oE 'title[^<>]*>[^<>]+' | cut -d'>' -f2 | sed -e "s/Index of//g" | tr -d ' '`
    REF_SID=`echo $RESPONSE | grep -oE 'b[^<>]*>[^<>]+' | cut -d'>' -f2 | awk '/[0-9]/ { print $0 }' | head -1`

    echo ">> Getting generated language model and dictionary..."
    curl -so lm $URL/$REF_URL/$REF_SID.lm
    curl -so dic $URL/$REF_URL/$REF_SID.dic

    echo ">> Language model and dictionary have been updated!"
else
    echo "Can't find file '$1'"
fi
