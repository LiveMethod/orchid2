<template>
  <div class="some-shit">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'SomeShit',
  data () {
    return {
      msg: 'Well, aint this some shit'
    }
  }
}
</script>

<style scoped lang="scss">
.some-shit{
  h1 {
    font-weight: normal;
    color: red;
  }
}
</style>
