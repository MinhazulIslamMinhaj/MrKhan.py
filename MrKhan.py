# MrKhan.pyname: Waka Readme
 
on:
  schedule:
    - cron: '30 18 * * *'
  workflow_dispatch:
jobs:
  update-readme:
    name: WakaReadme DevMetrics
    runs-on: ubuntu-latest
    steps:
      - uses: MrKhan404/waka-readme@master
        with:
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
          BLOCKS: ->
          TIME_RANGE: all_time
          SHOW_TIME: true
          SHOW_TITLE: true
          SHOW_MASKED_TIME: true
          LANG_COUNT: 7
          CODE_LANG: python
