# Mathilde's recipes GitHub Page

**Mathilde's recipes** is a project created that combines cooking and coding.

### Cooking objectives
1. Cook healthy & delicious meals on a regular basis
2. Figure out what groceries to get more efficiently
3. Figure out how much time each meal takes to prepare
4. Being able to check my recipes from anywhere 
 
### Coding objectives
I plan to learn programming on my spare time & I wish to write some programs that I could directly use from the Github page
1. Convert units (*e.g.* Celsius to Fahrenheit)
2. Select recipes with defined filters (*e.g.* preparation time) 
3. Generate grocery list based on future recipes

### Let's connect!
[![GitHub](assets/images/github.png){: .left-icon}GitHub](https://github.com/mbonnemaison/Recipes)

### How to run the site locally

[Clone](https://help.github.com/en/articles/cloning-a-repository) (or [fork](https://help.github.com/en/articles/about-forks) then clone) this repo.

Install Ruby v2.6+ as explained in the [Jekyll docs](https://jekyllrb.com/docs/installation/) for your operating system (via [rbenv](https://github.com/rbenv/rbenv), for example).

Make sure both the installed Ruby version and RubyGems are on your path:

```
$ ruby -v
$ gem -v
```

If the version of ruby on your system is too recent (e.g. version 3.0.1), install Ruby Version Manager or rvm. Instructions to install rvm are [here](https://rvm.io/rvm/install) and this [youtube video](https://www.youtube.com/watch?v=cQVb7fHFjSM) details how to use rvm to install and run previous versions of ruby. Briefly, once rvm is installed:
```
$ ruby -v
$ rvm -v
$ rvm use 2.6.0
$ ruby -v
```
*Note:*
If your terminal does not have access to rvm functions, you may get the following error:
```
RVM is not a function, selecting rubies with 'rvm use ...' will not work.

You need to change your terminal emulator preferences to allow login shell.
Sometimes it is required to use `/bin/bash --login` as the command.
Please visit https://rvm.io/integration/gnome-terminal/ for a example.
```
On Fedora (and [Ubuntu](https://stackoverflow.com/questions/23963018/rvm-is-not-a-function-selecting-rubies-with-rvm-use-will-not-work)), do as follow:
1. Open console
2. Go to Preferences
3. Go to Profiles > Command
4. Check box 'Run command as a login shell'
5. Restart terminal

You should be able to use rvm functions.

Install [Bundler](https://bundler.io/):

```
$ gem install bundler
```

Install the gems to build the site:

```
$ bundle install
```

Build and serve the site:

```
$ bundle exec jekyll serve
```

View the site in a browser at <http://localhost:4000>.

## Developing the site

This site uses the [Hydeout](https://fongandrew.github.io/hydeout/) theme. Most of the site's structure and style come from the theme.

To run Jekyll commands, use `bundle exec jekyll`.


*We thank the [Boston Python group](https://about.bostonpython.com) for allowing us to use their GitHub page as a model for our GitHub page.*
