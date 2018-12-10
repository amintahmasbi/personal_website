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

7. Develop before deploy. Hugo does not remove generated files before building. 

8. Start a server that builds draft content to check and modify the content with e.g., a `dev/` directory:
	```shell
	$ hugo server -D -d dev
	```
9. Run `hugo` to deploy to the `public` folder (or any personalized `publishDir` in `config.toml` file)

10. FLask

11. Flask run

12. Flask

13. Install the heroku command line tools and login:

    ```shell
    (venv) $ sudo snap install --classic heroku
    (venv) $ heroku login
    ```

14. Clone an existing app Or 

    ```bash
    (venv) $ heroku git:clone --recurse-submodules -a (my-unique-app-name)
    ```

15. Create a heroku app: (name is optional)

    ```shell
    (venv) $ heroku create (my-unique-app-name)	
    ```

16. Find and add the `hugo` buildpack:

    ```shell
    $ heroku buildpacks:search hugo
    $ heroku buildpacks:add roperzh/hugo
    $ heroku config:set HUGO_VERSION=0.52
    ```

17. Finally, deploy!

    ```shell
    $ git push heroku master
    $ heroku open
    ```

