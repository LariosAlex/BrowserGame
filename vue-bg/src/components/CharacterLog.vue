<template>
  <div>
    <!-- Botón para abrir el pop-up -->
    <button @click="openModal" class="bg-black hover:bg-green-600 text-white font-semibold py-2 px-4 rounded">CONSOLA</button>
  
    <!-- Pop-up -->
    <div v-if="isModalOpen" class="fixed inset-x-0 bottom-20 flex items-center justify-end right-5 z-50 max-h-30">
      <div class="bg-black w-1/5 border-2 border-green-400 p-4 relative" style="height: 500px">
        <ol class="relative border-l border-gray-200 dark:border-gray-700 h-full overflow-auto flex-grow">
          <li v-if="actions.length < 1" class="mb-10 ml-6">
            <p class="mb-4 text-base font-normal text-green-400 dark:text-white">NO S'HA EFECTUAT CAP ACCIÓ ENCARA</p>
          </li>
          <li v-else v-for="action in actions" :key="action" class="mb-10 ml-6">            
            <h3 class="flex items-center text-center mb-1 text-lg font-semibold text-green-400 dark:text-white">{{ action.action__name }}</h3>
            <time class="block mb-2 text-sm font-normal leading-none text-green-400 dark:text-white">{{ formatDateTime(action.datetime) }}</time>
            <p class="mb-4 text-base font-normal text-green-400 dark:text-white">% EXIT: {{ action.action__success_rate }}  -- TIRADA: {{ action.run_number }}</p>
            <p class="mb-4 text-base font-normal dark:text-white" :class="[action.succeed ? 'text-green-400' : 'text-red-400']">
              L'ACCIO {{ action.succeed ? "S'HA EXECUTAT AMB EXIT" : "HA ESTAT UN FRACAS" }}
            </p>
          </li>
        </ol>
      </div>
    </div>
  </div>
</template>
<script>
    export default {
      name: 'CharacterLog',
      data() {
        return {
            actions: null,
            character: null,
            loadingActions: true,
            isModalOpen: false,
        }
      },
      methods: {
        getCharacterLastActions: async function() {
          try {
            const getCharacterLoggedAPI = await fetch('api/getCharacterLogged');
            const dataCharacterLogged = await getCharacterLoggedAPI.json();
            this.character = dataCharacterLogged.character
            const getActionsAPI = await fetch(`/api/getLastActions/`+this.character.id);
            const dataActions = await getActionsAPI.json();
            this.actions = dataActions.actions;
            this.loadingActions = false;
          } catch (error) {
            console.error(error);
            this.loadingActions = false;
          }
        },
        openModal() {
          this.isModalOpen = !this.isModalOpen;
          this.getCharacterLastActions()
        },
        formatDateTime(dateTime) {
          const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' };
          return new Date(dateTime).toLocaleString('ca-ES', options);
        }
      },
      mounted() {
        this.getCharacterLastActions()
        setInterval(this.getCharacterLastActions, 30000);
      },
    }
    
    </script>