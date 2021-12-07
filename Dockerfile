FROM python:3 AS pelican

RUN pip install --no-cache-dir pelican

FROM node:16 as node

# change this to change the theme; make sure it matches `pelicanconf.py` though
ARG THEME_DIR=theme/feltnerm
WORKDIR /usr/src/$THEME_DIR

COPY $THEME_DIR/package*.json ./
COPY $THEME_DIR/index.js $THEME_DIR/postcss.config.js ./
COPY $THEME_DIR/src/ ./src
COPY $THEME_DIR/templates/ ./templates
RUN npm ci --ignore-scripts # `--ignore-scripts` to separate install and build into layers
RUN npm run build

FROM pelican AS site

WORKDIR /usr/src/site
COPY --from=1 /usr/src/theme/feltnerm/static ./theme/feltnerm/static

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY Makefile .
COPY pelicanconf.py publishconf.py ./
COPY plugins ./plugins
COPY content ./content

CMD [ "make",  "publish" ]
