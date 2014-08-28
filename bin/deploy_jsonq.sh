#!/bin/sh

rvm use 2.1.0
git checkout master
ruhoh compile
git checkout gh-pages
git clean -f -d -e .bundle -e Gemfile.lock -e compiled -n                                                        
git rm -rf . 
cp -r compiled/* .
rm -rf compiled
echo "jsonq.org" >> CNAME
echo "Gemfile.lock" >> .gitignore
git add .
git ci -m"update from master"
git push origin gh-pages
git checkout master
