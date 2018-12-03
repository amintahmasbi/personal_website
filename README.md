# Hugo + Flask + Heroku

1. install `hugo`

   ```shell
   $ snap install hugo --channel=extended
   ```

2. check installation

   ```shell
   $ hugo version
   Hugo Static Site Generator v0.52/extended linux/amd64 BuildDate: 2018-11-28T18:27:35Z
   
   ```

3. create a new site

   ```shell
   $ hugo new site personal_website
   $ cd personal_website
   $ git init
   ```

4. Add and modify `README.md` and `.gitignore` 

5. Make the first commit

6. Add a theme

   ```shell
   $ git submodule add https://github.com/cboettig/hugo-now-ui themes/hugo-now-ui
   $ echo 'theme = "hugo-now-ui"' >> config.toml
   ```

7. Check and modify the content with `$ hugo server -D`

8. Run `hugo` to deploy to the `public` folder (or any personalized `publishDir` in `config.toml` file)

9. dd

10. ddd

11. ddd

12. Install the heroku command line tools and login:

    ```shell
    (venv) $ sudo snap install --classic heroku
    (venv) $ heroku login
    ```

13. create a heroku app: (name is optional)

    ```shell
    (venv) $ heroku create (my-unique-app-name)	
    ```

14. Find and add the `hugo` buildpack:

    ```shell
    $ heroku buildpacks:search hugo
    $ heroku buildpacks:add roperzh/hugo
    $ heroku config:set HUGO_VERSION=0.52
    ```

15. Finally, deploy!

    ```shell
    $ git push heroku master
    $ heroku open
    ```

