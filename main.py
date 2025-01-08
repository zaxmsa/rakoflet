<Page xmlns="http://schemas.nativescript.org/tns.xsd" navigatingTo="navigatingTo" class="bg-white">
    <ActionBar title="Zax Translate" class="bg-white text-black">
        <NavigationButton visibility="collapsed" />
    </ActionBar>
    
    <GridLayout rows="*, auto" class="p-6">
        <!-- Language Selection -->
        <GridLayout row="0" rows="auto" columns="*" class="bg-blue-50 p-8 rounded-3xl" tap="{{ switchLanguages }}">
            <GridLayout rows="auto, auto" columns="*, auto, *">
                <!-- Source Language -->
                <StackLayout col="0" row="0" rowSpan="2" class="text-center">
                    <Label text="{{ sourceLanguage.code }}" class="text-4xl font-bold text-blue-600" />
                    <Label text="{{ sourceLanguage.name }}" class="text-lg text-gray-600 mt-1" />
                </StackLayout>
                
                <!-- Switch Icon -->
                <Label col="1" row="0" rowSpan="2" text="⇄" class="text-3xl text-gray-400" verticalAlignment="center" />
                
                <!-- Target Language -->
                <StackLayout col="2" row="0" rowSpan="2" class="text-center">
                    <Label text="{{ targetLanguage.code }}" class="text-4xl font-bold text-blue-600" />
                    <Label text="{{ targetLanguage.name }}" class="text-lg text-gray-600 mt-1" />
                </StackLayout>
            </GridLayout>
        </GridLayout>

        <!-- Start Button -->
        <Button row="1" text="تشغيل" tap="{{ startFloatingService }}" 
                class="bg-blue-600 text-white text-lg p-4 rounded-full w-32 self-center mt-8" />
    </GridLayout>
</Page>
