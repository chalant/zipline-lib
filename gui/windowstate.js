"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class WindowState {
    constructor(windowStateTracker) {
        this.windowStateTracker = windowStateTracker;
    }
    update(event) {
        return this._update(event, this.windowStateTracker);
    }
    handleAnimationEnd(event) {
        var tracker = this.windowStateTracker;
        this._handleAnimationEnd(event, tracker);
        tracker.mainWindow.stopAnimationLoop();
    }
    handleAnimationStart(event) {
        this.windowStateTracker.mainWindow.startAnimationLoop();
        this._handleAnimationStart(event, this.windowStateTracker);
    }
    _handleAnimationStart(event, windowStateTracker) {
    }
}
class InitialWindowState extends WindowState {
    _handleAnimationEnd(event, tracker) {
        // tracker.body.removeChild(tracker.outputWindow)
        // tracker.body.removeChild(this.titleBar)
    }
    _update(event, tracker) {
        if (event === 'run') {
            const outputtitleBar = this.titleBar = document.createElement('div');
            //buttons
            // const play = tracker.playButton = document.createElement('button')
            const quit = tracker.quitButton = document.createElement('button');
            const shrink = tracker.shrinkIcon = document.createElement('button');
            //icons
            // const playIcon = tracker.playIcon = document.createElement('i')
            const quitIcon = tracker.quitIcon = document.createElement('i');
            const shrinkIcon = tracker.shrinkIcon = document.createElement('i');
            const body = tracker.body;
            const output = tracker.outputWindow = document.createElement('div');
            //play
            // play.appendChild(playIcon)
            // play.id = "play"
            // playIcon.id = "play-icon"
            // playIcon.setAttribute('class', 'fas fa-play')
            //quit
            quit.appendChild(quitIcon);
            quit.id = "quit";
            quit.setAttribute('class', 'output-buttons');
            quitIcon.id = "quit-icon";
            quitIcon.setAttribute('class', 'fas fa-times output-buttons');
            //shrink
            shrink.appendChild(shrinkIcon);
            shrink.setAttribute('class', 'output-buttons');
            shrink.id = "shrink";
            shrinkIcon.id = "shrink-icon";
            shrinkIcon.setAttribute('class', 'fas fa-window-minimize');
            outputtitleBar.appendChild(quit);
            outputtitleBar.appendChild(shrink);
            outputtitleBar.id = 'output-titlebar';
            body.appendChild(outputtitleBar);
            body.appendChild(output);
            //register to button click events that affect the current state
            shrink.onclick = () => {
                tracker.currentState = tracker.currentState.update('shrink');
            };
            quit.onclick = () => {
                tracker.currentState = tracker.currentState.update('quit');
            };
            function animationEndHandler(ev) {
                tracker.currentState.handleAnimationEnd(ev);
            }
            function animationStartHandler(ev) {
                tracker.currentState.handleAnimationStart(ev);
            }
            const container = tracker.container;
            container.addEventListener('animationend', animationEndHandler);
            container.addEventListener('animationstart', animationStartHandler);
            return tracker.shrunkOuputWindow.update("run");
        }
        else if (event === 'quit') {
            //stop activity before quitting the window...
            tracker.body.removeChild(tracker.outputWindow);
            tracker.body.removeChild(this.titleBar);
            return this;
        }
        else if (event === 'shrink') {
            //nothing happens on the shrink event when in initial state...
            return this;
        }
        else {
            return this;
        }
    }
}
class StandbyOuputWindowState extends WindowState {
    _handleAnimationEnd(event, tracker) {
    }
    _update(event, tracker) {
        if (event === 'run') {
            return tracker.shrunkOuputWindow.update("run");
        }
        else if (event === 'quit') {
            tracker.activityStateTracker.update('stop');
            return this;
        }
    }
}
class ExpandedOutputWindowState extends WindowState {
    _handleAnimationEnd(event, tracker) {
        tracker.shrinkIcon.classList.remove('fa-window-restore');
        tracker.shrinkIcon.classList.add('fa-window-minimize');
    }
    _inner_update(event, tracker) {
        const container = tracker.container;
        if (event === 'shrink') {
            container.style.animation = "container-tran-expand 300ms ease-out";
            container.classList.remove("container-min-dims");
            container.classList.add("container-tran-dims");
            tracker.outputWindow.classList.replace('output-max-dims', 'output-min-dims');
            return tracker.shrunkOuputWindow;
        }
        else if (event === 'quit') {
            container.style.animation = "container-expand 300ms ease-out";
            container.classList.remove("container-min-dims");
            container.classList.add("container-max-dims");
            tracker.outputWindow.classList.remove('output-max-dims');
            return tracker.standbyOutputWindowState.update('quit');
        }
        else if (event === 'run') {
            tracker.activityStateTracker.update('run');
            return this;
        }
        else {
            return this;
        }
    }
    _update(event, tracker) {
        return this._inner_update(event, tracker);
    }
}
class ShrunkOutputWindowState extends WindowState {
    _handleAnimationEnd(event, tracker) {
        tracker.shrinkIcon.classList.remove('fa-window-minimize');
        tracker.shrinkIcon.classList.add('fa-window-restore');
    }
    _inner_update(event, tracker) {
        const output = tracker.outputWindow;
        const container = tracker.container;
        if (event === 'shrink') {
            container.style.animation = "container-tran-shrink 300ms ease-out";
            container.classList.remove("container-tran-dims");
            container.classList.add("container-min-dims");
            tracker.outputWindow.classList.replace('output-min-dims', 'output-max-dims');
            return tracker.expandedOutputWindow;
        }
        else if (event === 'run') {
            //creates and expands the output window
            output.id = 'output';
            container.style.animation = "container-shrink 300ms ease-out";
            container.classList.remove("container-max-dims");
            container.classList.add("container-min-dims");
            tracker.outputWindow.classList.add('output-max-dims');
            tracker.activityStateTracker.update("run");
            return tracker.expandedOutputWindow;
        }
        else if (event === 'quit') {
            container.style.animation = "container-tran-max-expand 300ms ease-out";
            container.classList.remove("container-tran-dims");
            container.classList.add("container-max-dims");
            output.classList.remove('output-min-dims');
            return tracker.standbyOutputWindowState.update('quit');
        }
        else {
            return this;
        }
    }
    _update(event, tracker) {
        return this._inner_update(event, tracker);
    }
}
class WindowStateTracker {
    constructor(activityStateTracker, mainWindow) {
        //states
        this.initialWindowState = new InitialWindowState(this);
        this.expandedOutputWindow = new ExpandedOutputWindowState(this);
        this.shrunkOuputWindow = new ShrunkOutputWindowState(this);
        this.standbyOutputWindowState = new StandbyOuputWindowState(this);
        this.currentState = this.initialWindowState;
        this.activityStateTracker = activityStateTracker;
        this.mainWindow = mainWindow;
        this.sideBar = document.getElementById('sidebar');
        //TODO: should create the buttons etc. here...
        const runButton = this.runButton = document.getElementById('run');
        this.body = document.getElementsByTagName('body')[0];
        this.container = document.getElementById('container');
        runButton.onclick = () => {
            this.currentState = this.currentState.update("run");
        };
    }
}
exports.WindowStateTracker = WindowStateTracker;
//# sourceMappingURL=windowstate.js.map