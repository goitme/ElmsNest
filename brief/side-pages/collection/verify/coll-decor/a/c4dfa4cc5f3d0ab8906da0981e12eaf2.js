try {
    Reflect.defineProperty(SliderComponent.prototype, 'initPages', {
        value: function () {
            if (!this || !this.sliderItems) return

            this.sliderItemsToShow = Array.from(this.sliderItems).filter(
                (element) => element.clientWidth > 0
            )
            if (this.sliderItemsToShow.length < 2) return
            this.sliderItemOffset =
                this.sliderItemsToShow[1].offsetLeft -
                this.sliderItemsToShow[0].offsetLeft
            this.slidesPerPage = Math.floor(
                Math.abs(
                    (this.slider.clientWidth +
                        this.sliderItemsToShow[0].offsetLeft) /
                        this.sliderItemOffset
                )
            )
            // console.log(
            //     'Step 1',
            //     this.slider.clientWidth + this.sliderItemsToShow[0].offsetLeft
            // )
            // console.log(
            //     'Step 2',
            //     (this.slider.clientWidth +
            //         this.sliderItemsToShow[0].offsetLeft) /
            //         this.sliderItemOffset
            // )
            // console.log(
            //     'Step 3',
            //     Math.abs(
            //         (this.slider.clientWidth +
            //             this.sliderItemsToShow[0].offsetLeft) /
            //             this.sliderItemOffset
            //     )
            // )
            // console.log(
            //     'Step 4',
            //     Math.floor(
            //         Math.abs(
            //             (this.slider.clientWidth +
            //                 this.sliderItemsToShow[0].offsetLeft) /
            //                 this.sliderItemOffset
            //         )
            //     )
            // )
            // console.log('slidesPerPage', this.slidesPerPage)

            // console.log('client width', this.slider.clientWidth)
            // console.log('+(this.sliderItemsToShow[0].offsetLeft)', +(this.sliderItemsToShow[0].offsetLeft))
            // console.log('calc:', (this.slider.clientWidth + +(this.sliderItemsToShow[0].offsetLeft)))
            // console.log('slidesPerPage', this.slidesPerPage);
            // console.log('Math.floor((this.slider.clientWidth + +(this.sliderItemsToShow[0].offsetLeft))', Math.floor((this.slider.clientWidth + +(this.sliderItemsToShow[0].offsetLeft))));
            // console.log('(this.slider.clientWidth + +(this.sliderItemsToShow[0].offsetLeft)', (this.slider.clientWidth + +(this.sliderItemsToShow[0].offsetLeft)));
            // console.log('slidesPerPage NOT ABS', Math.floor((this.slider.clientWidth + +(this.sliderItemsToShow[0].offsetLeft)) / this.sliderItemOffset));

            this.totalPages =
                this.sliderItemsToShow.length - this.slidesPerPage + 1

            this.update()
        },
    })
} catch (error) {}
