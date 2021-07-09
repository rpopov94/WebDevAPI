new Vue({
 el: '#map_app',
 data:{
     main_map:[]
 },
 created: function (){
     const vm = this
     axios.get('api/map')
         .then(function (response){
             //console.log(response.data)
             vm.main_map = response.data
         })
 }
})