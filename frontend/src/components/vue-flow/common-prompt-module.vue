<script lang="ts" setup>
import { ref } from 'vue'
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip'
import { Collapsible, CollapsibleTrigger, CollapsibleContent } from '@/components/ui/collapsible'
import { ChevronsUpDownIcon, AlertCircleIcon } from 'lucide-vue-next'
import { Textarea } from '@/components/ui/textarea'
import api from '@/api/api' //import the api module

const isOpen = ref(false)
const data = ref('')
const fetchData = async () => {
  try {
    const response = await api.getNodes()
    console.log('Fetched data:', response.data)
    // Process the fetched data as needed
  } catch (error) {
    console.error('Error fetching data:', error)
  }
}

const saveData = async () => {
  try {
    const node = { name: 'Default Name', prompt: data.value }
    const response = await api.createNode(node)
    console.log('Data saved:', response.data)
    // Process the saved data as needed
  } catch (error) {
    console.error('Error saving data:', error)
  }
}

// Fetch data when the component is mounted
fetchData()
</script>

<template>
  <div class="rounded-md bg-muted px-3 py-4">
    <Collapsible v-model:open="isOpen">
      <collapsible-trigger as-child>
        <div class="flex w-full items-center justify-between">
          <div class="flex items-center gap-x-2">
            <chevrons-up-down-icon class="h-4 w-4 cursor-pointer" />
            <p>Prompt</p>
            <tooltip-provider>
              <tooltip>
                <tooltip-trigger>
                  <alert-circle-icon class="h-3 w-3 text-muted-foreground" />
                </tooltip-trigger>
                <tooltip-content>
                  <p class="max-w-60" v-pre>
                    Enter the prompt words of the large model to implement the corresponding function. You can use the
                    {{ variable name }} method to introduce variables from the input parameters
                  </p>
                </tooltip-content>
              </tooltip>
            </tooltip-provider>
          </div>
        </div>
      </collapsible-trigger>
      <collapsible-content class="space-y-3 px-3 py-3">
        <Textarea
          placeholder="You can use the {{ variable name }} method to introduce variables from the input parameters"
          v-model="data"
        />
        <button @click="saveData">Save</button>
      </collapsible-content>
    </Collapsible>
  </div>
</template>
