trigger AccountTrigger on Account (before insert) {
    AccountDuplicateChecker.checkForDuplicates(Trigger.new);
}
