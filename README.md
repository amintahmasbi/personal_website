# Hugo + Flask + Heroku

Content for [my website](https://tahmasbi.net) which includes the theme, templates, how-to.

## 1. Setup Hugo and Create Static Content for the Website

1. install `hugo`

   ```shell
   $ snap install hugo --channel=extended
   ```

2. check installation

   ```shell
   $ hugo version
   Hugo Static Site Generator v0.52/extended linux/amd64 BuildDate: 2018-11-28T18:27:35Z
   
   ```

3. clone this repo

   ```bash
   $ git clone --recurse-submodules https://github.com/amintahmasbi/personal_website.git
   ```

   1. or create a new site:

   ```shell
   $ hugo new site personal_website
   $ cd personal_website
   $ git init
   ```

   2. Add and modify `README.md` and `.gitignore` 

   3. Make the first commit

   4. Add a theme

   ```shell
   $ git submodule add https://github.com/cboettig/hugo-now-ui themes/hugo-now-ui
   $ echo 'theme = "hugo-now-ui"' >> config.toml
   ```

4. Develop before deploy. Hugo does not remove generated files before building. 

5. Start a server that builds draft content to check and modify the content with e.g., a `dev/` directory:
  ```shell
  $ hugo server -D -d dev
  ```

6. Run `hugo` to deploy to the `public` folder (or any personalized `publishDir` in `config.toml` file)

## 2. Setup Flask and Create Dynamic Content of the Website

_Note_: You can skip this section if you do not have any dynamic content to add.

1. FLask
2. Flask run
3. Flask

##3. Setup Heroku and deploy the website 

1. Install the heroku command line tools and login:

  ```shell
  (venv) $ sudo snap install --classic heroku
  (venv) $ heroku login
  ```

2. Clone an existing app 

   ```bash
   (venv) $ heroku git:clone --recurse-submodules -a (my-unique-app-name)
   ```

   1. Or create a new heroku app: (name is optional)

   ```shell
   (venv) $ heroku create (my-unique-app-name)	
   ```

3. Find and add the `hugo` buildpack:

   ```shell
   $ heroku buildpacks:search hugo
   $ heroku buildpacks:add roperzh/hugo
   $ heroku config:set HUGO_VERSION=0.52
   ```

4. Commit the changes 

5. Finally, deploy!

   ```shell
   $ git push heroku master
   $ heroku open
   ```

## License 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details