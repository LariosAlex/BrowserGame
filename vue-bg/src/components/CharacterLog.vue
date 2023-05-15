<template>
  <div>
    <!-- Botón para abrir el pop-up -->
    <button @click="openModal" class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded">Abrir Pop-up</button>
  
    <!-- Pop-up -->
    <div v-if="isModalOpen" class="fixed inset-0 flex items-center justify-center z-50">
      <div class="fixed inset-0 bg-black opacity-50"></div> <!-- Fondo oscuro bloqueador -->
      <div class="bg-white w-1/5 border-2 border-black p-4 relative">
        <ol class="relative border-l border-gray-200 dark:border-gray-700">                  
          <li v-for="action in actions" :key="action" class="mb-10 ml-6">            
            <span class="absolute flex items-center justify-center w-6 h-6 bg-blue-100 rounded-full -left-3 ring-8 ring-white dark:ring-gray-900 dark:bg-blue-900">
              <svg aria-hidden="true" class="w-3 h-3 text-blue-800 dark:text-blue-300" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path></svg>
            </span>
            <h3 class="flex items-center mb-1 text-lg font-semibold text-gray-900 dark:text-white">{{ action.action__name }}</h3>
            <time class="block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">{{ action.datetime }}</time>
            <p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">{{ action.performer__nickname }}</p>
          </li>
        </ol>
        <button @click="closeModal" class="absolute top-2 right-2 text-gray-500 hover:text-gray-800 dark:text-gray-400 dark:hover:text-gray-200">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
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
          this.isModalOpen = true;
        },
        closeModal() {
          this.isModalOpen = false;
        }
      },
      mounted() {
        this.getCharacterLastActions()
        setInterval(this.getCharacterLastActions, 30000);
      },
    }
    </script>