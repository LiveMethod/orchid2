<template>
  <div class="month-select-bar">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'MonthSelectBar',
  data () {
    return {
      msg: 'Well, aint this some shit'
    }
  }
}
</script>

<style scoped lang="scss">
.month-select-bar{
  h1 {
    font-weight: normal;
    color: red;
  }
}
</style>
