<template>
  <div v-if="!loadingActions" class="grid grid-cols-4 auto-cols-fr gap-4 bg-black w-4/5 mx-auto flex justify-center items-center p-5">
    <div v-for="action in actions" :key="action.id" class="w-full max-w-sm border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
    :class="{
      'bg-orange-100': action.category === 'PAS',
      'bg-green-100': action.category === 'DEF',
      'bg-red-100': action.category === 'OFF'
    }"
    >
        <div class="flex justify-end px-4 pt-4"></div>
        <div class="flex flex-col items-center pb-10">
            <img class="w-24 h-24 mb-3 rounded-full shadow-lg bg-white" src="../assets/revolver.png" alt="{{ action.name }}"/>
            <h5 class="mb-1 text-xl font-medium text-gray-900 dark:text-white">{{ action.name }} - {{ action.cost }}</h5>
            <div>
              <span class="text-sm text-gray-500 dark:text-gray-400">{{ action.category }}</span>
              <span class="flex items-center text-sm font-medium text-gray-900 dark:text-white"><span class="flex w-2.5 h-2.5 bg-orange-700 rounded-full mr-1.5 flex-shrink-0"></span>{{ action.mana }}</span>
              <span class="flex items-center text-sm font-medium text-gray-900 dark:text-white"><span class="flex w-2.5 h-2.5 bg-green-700 rounded-full mr-1.5 flex-shrink-0"></span>{{ action.health }}</span>
              <span class="flex items-center text-sm font-medium text-gray-900 dark:text-white"><span class="flex w-2.5 h-2.5 bg-red-700 rounded-full mr-1.5 flex-shrink-0"></span>{{ action.damage }}</span>
              <span class="flex items-center text-sm font-medium text-gray-900 dark:text-white"><span class="flex w-2.5 h-2.5 bg-blue-700 rounded-full mr-1.5 flex-shrink-0"></span>{{ action.exp }}</span>
            </div>
            <div class="flex mt-4 space-x-3 md:mt-6">
                <a @click="rechargeCharactreItems" class="inline-flex items-center px-4 py-2 text-sm font-medium text-center text-white rounded-lg focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                :class="{
                  'bg-orange-300 hover:bg-orange-700 border-orange-700': action.category === 'PAS',
                  'bg-green-300 hover:bg-green-700 border-green-700': action.category === 'DEF',
                  'bg-red-300 hover:bg-red-700 border-red-700': action.category === 'OFF'
                }"
                >EXECUTAR ACCIÓ</a>
            </div>
        </div>
    </div>
  </div>
</template>
  
<script>
    export default {
    name: "ActionButtons",
    data() {
        return {
            actions: null,
            loadingActions: true,
        };
    },
    methods: {
        getActions: async function () {
            try {
                const response = await fetch("/api/getActions");
                const data = await response.json();
                this.actions = data.actions;
                this.loadingActions = false;
            }
            catch (error) {
                console.error(error);
                this.loadingActions = false;
            }
        },

        rechargeCharactreItems(){
          this.$emit('recargar-items');
        }

        /*funcionesDeLasAcciones(){
          FuncionQueLlamaAnimacion
          FuncionQueGuardaLosDatos
        } */
    },
    mounted() {
        this.getActions();
    },
}
</script>
